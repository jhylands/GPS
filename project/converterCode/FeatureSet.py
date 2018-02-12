import numpy as np
from datetime import datetime

#https://stackoverflow.com/questions/9647202/ordinal-numbers-replacement
ordinal = lambda n: "%d%s" % (n,"tsnrhtdd"[(n/10%10!=1)*(n%10<4)*n%10::4])
AND = (lambda a,b:a and b)
#What I want this class to be able to input a data and be able to output the 2d array of the dataset

#keys for the feature vector string 
#Acting on speed or acceloration 
#mean  
#median
#mode  
#min
#max
#percentile

class FeatureSet():    
    #differntiate an array
    @staticmethod
    def dtripdt(x,t):
	return [(x2-x1)/(t2-t1).total_seconds() for (x1,x2,t1,t2) in zip(x[:-1],x[1:],t[:-1],t[1:])]

#for both the time and speed feilds should do a type check to make sure the 
#structure of the array is what you think it is
    #get the time fields from the data 
    @staticmethod
    def getTime(data):
	assert(reduce(AND,[[len(x)==4 for x in trip] for trip in data.iteritems()]))
	print data['\"515\"'][0][3]
	return [[datetime.strptime(t, '%Y-%m-%d %H:%M:%S') for TripID,PointID,v,t in trip] for key,trip in data.iteritems()]
    #get the speed fields from the data 
    @staticmethod
    def getSpeed(data):
	assert(reduce(AND,[[len(x)==4 for x in trip] for trip in data.iteritems()]))
	return [[v for TripID,PointID,v,t in trip] for key,trip in data.iteritems()]


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
	    self.dOFx[1] = [self.dtripdt(trip) for trip in dnx]
	    self.dOFx[2] = [self.dtripst(trip) for trip in self.dOFx[1]]
	self.columns = []
	self.headings=[]

    #This function is to return the data
    #Needs to be able to take the information in, in J form 
    def retrive(self):
	return self.columns

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

    def percentile(self,tiles,d):
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

