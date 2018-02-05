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

#within the car count how many are going above 80mph
carTot = len(flatten(car))
illCar = len(flatten([[speed for speed in trip if speed>80] for trip in getTripsSpeeds(car)]))
illCar1 = len(flatten([[speed for speed in trip if speed>70] for trip in getTripsSpeeds(car)]))
print "car 80:"
print float(illCar)/carTot *100
print "car 70:"
print float(illCar1)/carTot *100

#within walking how many ae going above 10mph
walkTot = len(flatten(walk))
illWalk = len(flatten([[speed for speed in trip if speed>5] for trip in getTripsSpeeds(walk)]))
print "walk 5:"
print float(illWalk)/walkTot *100


#within bus how many are going above 70mph
busTot = len(flatten(walk))
illBus = len(flatten([[speed for speed in trip if speed>70] for trip in getTripsSpeeds(bus)]))
illBus1 = len(flatten([[speed for speed in trip if speed>60] for trip in getTripsSpeeds(bus)]))
print "bus 70:"
print float(illBus)/busTot *100
print "bus 60:"
print float(illBus1)/busTot *100
