import os,csv,numpy,json
#get a list of the files
folder =  os.listdir('../gps')
folder = folder[1:] #miss out the .DS_Store file
files = []
for dire in folder:
	with open('../gps/' + dire + '/gps_points.csv') as f:
		files +=f.read().splitlines()
with open('gps_points.csv','w') as f:
	for file in files:
		f.write(file + '\n')
