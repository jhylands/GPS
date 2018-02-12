#This program takes the json files in and genrates a csv
import json, sys
from FeatureSet import FeatureSet
name = sys.argv[1]

with open(name,'r') as f:
    data =json.loads(f.read())
#Declare a set of features to be used.
#for each trip create a velocity and time
T = FeatureSet.getTime(data)
d1x = FeatureSet.getSpeed(data)
fs = FeatureSet(d1x,1,T)
fs.mean(1)
fs.mean(2)

data = fs.retrive()
with open('out.csv','w+') as f:
    f.write('\n'.join([','.join([str(e) for e in row]) for row in data]))

