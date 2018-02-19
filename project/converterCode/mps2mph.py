#Simple python program to convert json files in meters per second to a json file for miles per hour 
import json, sys

def convE2I(mps):
    mph = mps*2.23694
    return mph
def convI2E(mph):
    mps = mph*0.44704
    return mps

def update(point,index):
    #0 is the index of the speed
    point[index] = convI2E(point[index])
    return point

name = sys.argv[1]
with open(name,'r') as f:
    data = json.loads(f.read())
#meters to miles
#data = [[update(point,0) for point in trip] for trip in data]
#miles to meters
data = [[update(point,2) for point in trip] for key,trip in data.iteritems()]
name = sys.argv[2]
with open(name,'w+') as f:
    f.write(json.dumps(data))

print 'fin'
