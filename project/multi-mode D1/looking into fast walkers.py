import json
def getTripsSpeeds(trips):
	return [[float(a[2]) for a in trip] for trip in trips]

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
car = [trip for trip in trips if int(trip[0][1])==3 or int(trip[0][1])==4]
walk = [trip for trip in trips if int(trip[0][1])==1]
bus = [trip for trip in trips if int(trip[0][1])==6]


print car[0][0]

pureWalk = [trip for trip in getTripsSpeeds(walk) if max(trip)<50]
print "pureWalk:"
print len(pureWalk)
#lets look deaper into this walking
