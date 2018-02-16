#Simple python program to convert json files in meters per second to a json file for miles per hour 
import json, sys

def conv(mps):
    mph = mps*2.23694
    return mph
def update(point):
    #0 is the index of the speed
    point[0] = conv(point[0])
    return point

with open(name,'r') as f:
    data = json.loads(f.read())

data = [[update(point) for point in trip] for trip in data]

with open(name,'w+') as f:
    f.write(json.dumps(data))

print 'fin'
