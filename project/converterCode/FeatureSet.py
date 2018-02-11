import numpy as np
#https://stackoverflow.com/questions/9647202/ordinal-numbers-replacement
ordinal = lambda n: "%d%s" % (n,"tsnrhtdd"[(n/10%10!=1)*(n%10<4)*n%10::4])
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
    self.dxNames = ['position','speed','acceleration','jerk'] 
    #differntiate an array
    def dtripdt(x,t):
	return [(x2-x1)/(t2-t1) for (x1,x2,t1,t2) in zip(x[:-1],x[1:],t[:-1],t[1:])]


    #The class needs to be given the data; which needs to be in J format
    def __init__(self,data):
	self.dOFx = [[],[],[],[]]
	self.dOFx[1] = data #speeds
	self.dOFx[2] = [self.dtripdt(trip) for trip in data]
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
	self.columns.append([np.min(trip) for trip in self.dOFx[d])

    def max(self,d):
	self.headings.append('Max ' + self.dxNames[d])
	self.columns.append([np.max(trip) for trip in self.dOFx[d])

    #standard deviation
    def STD(self,d):
	self.headings.append('Standard deviation of ' + self.dxNames[d])
	self.columns.append([np.std(trip) for trip in self.dOFx[d])

    def percentile(self,tiles,d):
	#quatiles 1,10,25,75,90,99
	tiles = tiles || [1,10,25,75,90,99] 
	#CummulativeFrequenceySpeed
	CFS = []
	for tile in tiles:
		self.columns.append( [np.percentile(trip,tile) for trip in STD])
		self.headers.append( str(tile) + ordinal(tile) + ' Percentile of ' + self.dxNames[d])

    def Qrange(self,d)
	self.headings.append('Interquatile range of the ' + self.dxNames[d] + 's')
	Qrange = [np.percentile(trip,75)-np.percentile(trip,25) for trip in self.dOFx[d]]
	self.columns.append(Qrange)

