import numpy as np
from datetime import datetime,timedelta

#https://stackoverflow.com/questions/9647202/ordinal-numbers-replacement
ordinal = lambda n: "%d%s" % (n,"tsnrhtdd"[(n/10%10!=1)*(n%10<4)*n%10::4])
AND = (lambda a,b:a and b)
#What I want this class to be able to input a data and be able to output the 2d array of the dataset


class FeatureSet():    
    #differntiate an array
    #Does not work on distance array -> must be displacement
    @staticmethod
    def dtripdt(x,t):
	assert(isinstance(t[0],datetime))
	assert(isinstance(x[0],float))
	try:
	    return [abs(x2-x1)/np.max([(t2-t1).total_seconds(),1]) for x1,x2,t1,t2 in zip(x[:-1],x[1:],t[:-1],t[1:])]
	except ZeroDivisionError:
	    for t1,t2 in zip(t[1:],t[:-1]):
		print str(t1) + str(t2) + str(t2-t1)

#for both the time and speed feilds should do a type check to make sure the 
#structure of the array is what you think it is
    #get the time fields from the data 
    @staticmethod
    def getTime(data):
	if isinstance(data, dict):
	    assert(reduce(AND,[[len(x)==4 for x in trip] for trip in data.iteritems()]))
	    return [[datetime.strptime(t, '%Y-%m-%d %H:%M:%S') for TripID,PointID,v,t in trip] for key,trip in data.iteritems()]
	else:
	    assert(reduce(AND,[[len(x)==2 for x in trip] for trip in data]))
	    #some datetime from seconds
	    #return [[timedelta(0,point[1]) for point in trip if isinstance(point[1],float)] for trip in data]
	    return [[datetime.strptime(t,'%Y-%m-%d %H:%M:%S') for x,t in trip] for trip in data]
 
    #get the posion based data fields from the data 
    @staticmethod
    def getdnx(data):
	if isinstance(data, dict):
	    assert(reduce(AND,[[len(x)==4 for x in trip] for trip in data.iteritems()]))
	    return [[v for TripID,PointID,v,t in trip] for key,trip in data.iteritems()],1
	else:
	    assert(reduce(AND,[[len(x)==2 for x in trip] for trip in data]))
	    #some distances
	    return [[x for x,t in trip]  for trip in data],0

    #The class needs to be given the data; which needs to be in J format
    #The input to the class is an array of arrays each containing the nth derivitive of smome dataset over some time t
    def __init__(self,dnx,n,t): 
	#The input must be either position data or a derivitive thereof
	assert(n>=0 and n<=4)
    	self.dxNames = ['position','speed','acceleration','jerk'] 
	self.dOFx = [[],[],[],[]]
	self.dOFx[n] = dnx #speeds
	#not sure if I should included something that make the position data, not sure if it would be useful
	if(n==1):
	    self.dOFx[2] = [self.dtripdt(X,T) for X,T in zip(dnx,t)]
	elif(n==0):
	    self.dOFx[1] = [self.dtripdt(X,T) for X,T in zip(dnx,t)]
	    self.dOFx[2] = [self.dtripdt(X,T) for X,T in zip(self.dOFx[1],t)]
	self.columns = []
	self.headings=[]

    #This function is to return the data
    #Needs to be able to take the information in, in J form 
    def retrive(self):
	return np.transpose(self.columns)
    #returns a string to be written to file, this includes headings
    def getCSV(self):
	headingString = '"'+ '","'.join(self.headings) + '"\n'
	return headingString + '\n'.join([','.join([str(e) for e in row]) for row in self.retrive()]) 

    def printHeadings(self):
	print '|'.join(self.headings)
    def mean(self,d):
	self.headings.append('Mean ' + self.dxNames[d])
	self.columns.append([np.mean(trip) for trip in self.dOFx[d]])	

    def median(self,d):
	self.headings.append('Median ' + self.dxNames[d])
	self.columns.append([np.median(trip) for trip in self.dOFx[d]])

    def min(self,d):
	self.headings.append('Min ' + self.dxNames[d])
	self.columns.append([np.min(trip) for trip in self.dOFx[d]])

    def max(self,d):
	self.headings.append('Max ' + self.dxNames[d])
	self.columns.append([np.max(trip) for trip in self.dOFx[d]])

    #standard deviation
    def STD(self,d):
	self.headings.append('Standard deviation of ' + self.dxNames[d])
	self.columns.append([np.std(trip) for trip in self.dOFx[d]])

    def percentile(self,d,tiles):
	#quatiles 1,10,25,75,90,99
	tiles = tiles or [1,10,25,75,90,99] 
	#CummulativeFrequenceySpeed
	CFS = []
	for tile in tiles:
		self.columns.append( [np.percentile(trip,tile) for trip in self.dOFx[d]])
		self.headers.append( str(tile) + ordinal(tile) + ' Percentile of ' + self.dxNames[d])

    def Qrange(self,d):
	self.headings.append('Interquatile range of the ' + self.dxNames[d] + 's')
	Qrange = [np.percentile(trip,75)-np.percentile(trip,25) for trip in self.dOFx[d]]
	self.columns.append(Qrange)

