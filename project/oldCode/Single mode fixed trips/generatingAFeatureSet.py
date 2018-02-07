#we want to generate the feature set for each of the getTripsSpeeds(trips)
import json
import numpy as np

def getTripsSpeeds(trips):
	return [[float(a[3]) for a in trip] for trip in trips]

with open('data.json','r') as f:
	trips = json.loads(f.read())
#define an x gap
dx=3
#speedTripData
STD = getTripsSpeeds(trips)
#modeTripsData
MTD = [trip[0][2] for trip in trips]

print 'MTD:'
print len(MTD)

#Creating feature set

#means
means = [np.mean(trip) for trip in STD]
print 'Means:'
print len(means)
#medians
medians = [np.median(trip) for trip in STD]
print 'Medians:'
print len(medians)
#interquatile range
Qrange = [np.percentile(trip,75)-np.percentile(trip,25) for trip in STD]
print 'Qrange:'
print len(Qrange)
#absolute range

#max

#min

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

#mean acceloration
Ameans = [np.mean(trip) for trip in acc]

#median acceloration 
Amedians = [np.median(trip) for trip in acc]

#min
Amin =[np.min(trip) for trip in acc]

#max
Amax = [np.max(trip) for trip in acc]

#quatiles
#CumulativeFrequencyAcceloration
CFA=[]
for tile in tiles:
	CFA.append([np.percentile(trip,tile) for trip in acc])


featureSet = [MTD,means,medians,Qrange,Ameans,Amedians,Amin,Amax] + CFS + CFA

print len(featureSet)
for x in xrange(0,13):
	print str(x) + ":" + str(len(featureSet[x]))
featureSet = np.transpose(featureSet)
print len(featureSet)

with open('featureSet1.csv','w') as f:
	for row in featureSet:
		f.write(','.join([str(elm) for elm in row]) + '\n')





