import os,csv,numpy,json
#get a list of the files
folder =  os.listdir('../gps')
folder = folder[1:] #miss out the .DS_Store file
files = []
for dire in folder:
	with open('../gps/' + dire + '/gps_points.csv') as f:
		files.append([a.split(',') for a in f.read().splitlines()])
#Journies container is a list containing journies
#where each journey is represented as a list of gps points
blocks = []
for file in files:
	print 'F'
	traces = list(zip(*file))[2]
	mx = max(traces[1:]) #get the number of trips exluding the title
	#find the pivot 
	for trip in xrange(1,int(mx)):
		blocks.append([point for point in file[1:] if int(point[2])==trip])



#with the generated journiesContainer
#we can do the statistical analysis we want 

with open('data.pydat','w+') as f:
	f.write(json.dumps(blocks));
print 'fin'
