import json
from matplotlib import pyplot as plt
with open('data.json','r') as f:
	trips = json.loads(f.read())
#print zip(*trips)[0]
#segregate by mode
car = [trip for trip in trips if int(trip[0][1])==3 or int(trip[0][1])==4]
walk = [trip for trip in trips if int(trip[0][1])==1]
bus = [trip for trip in trips if int(trip[0][1])==6]

#function to get an array of trip speeds
def getTripsSpeeds(trips):
	return [[float(a[2]) for a in trip] for trip in trips]

def flatten(arr):
	beef =[]
	for trip in arr:
		beef += trip
	return beef

def prep(data):
	return flatten(getTripsSpeeds(data))

def pairs(l, func):
	pairs = []
	for i in xrange(len(l)-1):
		pairs.append(func(l[i],l[i+1]))
	return pairs

def diff(a,b):
	return b-a

def acceloration(data):
	return pairs(data,diff)

plt.boxplot([prep(walk),prep(car),prep(bus)])
plt.xticks([1,2,3],['walk','car','bus'])
plt.title('Speed Distribution')
plt.show()