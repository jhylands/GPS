#program to get the GPS data from strava gpx files
import gpxpy
import numpy as np

from gpxpy.geo import length

def speedTime(file):
	f = open('../Runs/' + file,'r')
	gpx = gpxpy.parse(f)
	for track in gpx.tracks:
		for segment in track.segments:
			print len(segment.points)
			points = segment.points
			D = [ p2.distance_3d(p1) for p1,p2 in zip(points[:-1],points[1:])]
			T = [ p2.time-p1.time for p1,p2 in zip(points[:-1],points[1:])]
			DT = [(d,t) for d,t in zip(D,T)]
			speeds = [ distance/time.total_seconds() for distance,time in DT ]
			return speeds,DT

def vector(arrSpeed):
	speed,DT = arrSpeed
	#more duration than times
	distances = [d for d,t in DT]
	T = [t.total_seconds() for d,t in DT]
	#speed
	#mean
	mean = np.average(speed,weights=T)
	#median
	median = np.median(speed)
	#Qrange
	Qrange = np.percentile(speed,75)-np.percentile(speed,25)
	tiles = [1,10,25,75,90,99]
	#CummulativeFrequenceySpeed
	CFS = []

	for tile in tiles:
		CFS.append(np.percentile(speed,tile))

	#estimation based on assuming 1 second intervals	
	dx = 1
	acceleration = [(b-a)/dx for (a,b) in zip(speed[:-1],speed[1:])]
	
	Amean = np.mean(acceleration)
	Amedian = np.median(acceleration)
	Qrange = np.percentile(acceleration,75)-np.percentile(acceleration,25)
	Amin = np.min(acceleration)
	Amax = np.max(acceleration)
	#quatiles
	#CumulativeFrequencyAcceloration
	CFA=[]
	for tile in tiles:
		CFA.append(np.percentile(acceleration,tile))
	featureSet = [9,mean,median,Qrange,Amean,Amedian,Amin,Amax] + CFS + CFA
	return featureSet

import os
traces = []
files = os.listdir("../Runs")
for file in files:
	if file.endswith(".gpx"):
		print str(len(traces)) + "/" + str(len(files))
		traces.append(vector(speedTime(file)))

with open('featureSetRun.csv','w') as f:
	for row in traces:
		f.write(','.join([str(elm) for elm in row]) + '\n')

