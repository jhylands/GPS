import numpy as np
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
    #The class needs to be given the data; which needs to be in J format
    def __init__(self,data):
	self.data = data

   #This function is to return the data, how one requests the information form this class I'm not sure yet :/
    #Needs to be able to take the information in, in J form 
    def retrive(self, headings):
	validate(headings)
	for(heading in headings):
		result.append(self.funcDic[heading])
    def wrap(self):

    def mean(self):
	self.meanSpeed = [np.mean(trip) for trip in self.data]
    def median(self):
	medians = [np.median(trip) for trip in self.data]
    def Qrange(self):
	Qrange = [np.percentile(trip,75)-np.percentile(trip,25) for trip in self.data]
	#quatiles 1,10,25,75,90,99

	tiles = [1,10,25,75,90,99]
	#CummulativeFrequenceySpeed
	CFS = []

	for tile in tiles:
		CFS.append( [np.percentile(trip,tile) for trip in STD] )
#Calculate equivelent acceloration data 
def dtripdt(trip):
	return [(b-a)/dx for (a,b) in zip(trip[:-1],trip[1:])]

acc = [dtripdt(trip) for trip in STD]

for x in xrange(0,13):
	print str(x) + ":" + str(len(featureSet[x]))
featureSet = np.transpose(featureSet)
print len(featureSet)

with open('featureSet1.csv','w') as f:
	for row in featureSet:
		f.write(','.join([str(elm) for elm in row]) + '\n')

