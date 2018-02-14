#what do we want from this file?

#well, we want the json file
#what we need is the matricies
#program to get the GPS data from strava gpx files
import gpxpy
import numpy as np

import os,sys,json
from gpxpy.geo import length

def speedTime(name,file):
	f = open(name + file,'r')
	gpx = gpxpy.parse(f)
	for track in gpx.tracks:
		for segment in track.segments:
			print len(segment.points)
			points = segment.points
			D = [ p2.distance_3d(p1) for p1,p2 in zip(points[:-1],points[1:])]
			T = [ p.time.strftime('%Y-%m-%d %H:%M:%S') for p in points[:-1]]
			DT = [(d,t) for d,t in zip(D,T)]
			#speeds = [ distance/time for distance,time in DT ]
			return DT
traces = []
assert(len(sys.argv)==3)
name = sys.argv[1]
files = os.listdir(name)
for file in files:
	if file.endswith(".gpx"):
		print str(len(traces)) + "/" + str(len(files))
		traces.append(speedTime(name,file))
name = sys.argv[2]
with open(name,'w+') as f:
    f.write(json.dumps(traces))

#with open('featureSetRun.csv','w') as f:
#	for row in traces:
#		f.write(','.join([str(elm) for elm in row]) + '\n')

