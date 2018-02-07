import os,csv,numpy,json
#get a list of the files
def toInt(S):
	return int(S.replace('"',''))
def  toString(S):
	return S.replace('"','')
def toFloat(S):
	return float(S.replace('"',''))
def point2point(point):
	return [toInt(point[0]),toString(point[1]),toInt(point[2]),toFloat(point[3]),toString(point[4])]

#Journies container is a list containing journies
#where each journey is represented as a list of gps points
blocks = []
with open('SingleModeTrips.csv','r') as f:
	file = [a.split(',') for a in f.read().splitlines()]

traces = [toInt(a) for a in list(zip(*file))[0]]

#find the pivot 
for trip in set(traces):
	print 'add' + str(trip)
	blocks.append([point2point(point) for point in file if toInt(point[0])==trip])



#with the generated journiesContainer
#we can do the statistical analysis we want 

with open('data.json','w+') as f:
	f.write(json.dumps(blocks));
print 'fin'
