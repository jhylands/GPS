import os,csv,numpy,json
#get a list of the files

#Journies container is a list containing journies
#where each journey is represented as a list of gps points
blocks = []
with open('Trips.csv','r') as f:
	file = [a.split(',') for a in f.read().splitlines()]

traces = [int(a.replace('"','')) for a in list(zip(*file))[0]]

#find the pivot 
for trip in set(traces):
	print 'add' + str(trip)
	blocks.append([point for point in file if int(point[0])==trip])



#with the generated journiesContainer
#we can do the statistical analysis we want 

with open('data.json','w+') as f:
	f.write(json.dumps(blocks));
print 'fin'
