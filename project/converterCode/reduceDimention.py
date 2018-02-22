#simple file to reduce the number of fields of the naturel data so it can be in the same form as the strava data

import json,sys

name = sys.argv[1]

with open(name,'r') as f:
    data = json.loads(f.read())
data = [[[point[2],point[3]] for point in trip if len(point)==4] for trip in data]

name = sys.argv[2]
with open(name,'w+') as f:
    f.write(json.dumps(data))

