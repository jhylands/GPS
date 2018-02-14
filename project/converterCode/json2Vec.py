#This program takes the json files in and genrates a csv
import json, sys
from FeatureSet import FeatureSet
name = sys.argv[1]

with open(name,'r') as f:
    data =json.loads(f.read())
#Declare a set of features to be used.
#for each trip create a velocity and time
T = FeatureSet.getTime(data)
dnx,n = FeatureSet.getdnx(data)
fs = FeatureSet(dnx,n,T)
fs.mean(1)
fs.mean(2)
fs.median(1)
fs.max(2)

fs.printHeadings()
data = fs.getCSV()
name = sys.argv[2]
with open(name,'w+') as f:
    f.write(data)

