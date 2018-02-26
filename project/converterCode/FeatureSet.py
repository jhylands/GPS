import numpy as np
from datetime import datetime,timedelta

#https://stackoverflow.com/questions/9647202/ordinal-numbers-replacement
ordinal = lambda n: "%d%s" % (n,"tsnrhtdd"[(n/10%10!=1)*(n%10<4)*n%10::4])
AND = (lambda a,b:a and b)
#What I want this class to be able to input a data and be able to output the 2d array of the dataset


class FeatureSet():    

    #The class needs to be given the data; which needs to be in J format
    #The input to the class is an array of arrays each containing the nth derivitive of smome dataset over some time t
    def __init__(self,FormJ): 
    	self.dxNames = ['position','speed','acceleration'] 
	self.dOFx = [[],[],[]]
	for x in [0,1,2]:
	    self.dOFx[x] =  [[point[x] for point in trip] for trip in FormJ]
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

