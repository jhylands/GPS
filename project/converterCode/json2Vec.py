#This program takes the json files in and genrates a csv
import json, sys
from FeatureSet import FeatureSet
name = sys.argv[1]

with open(name,'r') as f:
    data =json.loads(f.read())
#Declare a set of features to be used.
#for each trip create a velocity and time
fs = FeatureSet(data)
#speed
fs.mean(1)
fs.median(1)
fs.Qrange(1)
fs.percentile(1)
#acceloration
fs.mean(2)
fs.median(2)
fs.min(2)
fs.max(2)
fs.percentile(2)

fs.printHeadings()
data = fs.getCSV()
name = sys.argv[2]
with open(name,'w+') as f:
    f.write(data)

