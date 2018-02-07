import json
from matplotlib import pyplot as plt
def getTripsSpeeds(trips):
	return [[float(a[3]) for a in trip] for trip in trips]

def flatten(arr):
	beef =[]
	for trip in arr:
		beef += trip
	return beef

def prep(data):
	return flatten(getTripsSpeeds(data))

from matplotlib import pyplot as plt
with open('data.json','r') as f:
	trips = json.loads(f.read())
#print zip(*trips)[0]
#segregate by mode
car = [trip for trip in trips if int(trip[0][2])==3 or int(trip[0][2])==4]
bike = [trip for trip in trips if int(trip[0][2]==2)]
walk = [trip for trip in trips if int(trip[0][2])==1]
bus = [trip for trip in trips if int(trip[0][2])==6]

print len(bike)
print len(car)
print len(walk)
print len(bus)

pureWalk = [trip for trip in getTripsSpeeds(walk) if max(trip)<5]
print "pureWalk:"
print len(pureWalk)

#lets look deaper into this walking
for i in xrange(0,36):
	plt.subplot(6,6,i-10)

	plt.plot(getTripsSpeeds(walk)[i])
plt.show()
