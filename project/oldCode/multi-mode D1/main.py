import json
import numpy as np
from matplotlib import pyplot as plt
from datetime import datetime

with open('data.pydat','r') as f:
	blocks = json.loads(f.read())

speedss = [[float(col[6]) for col in block] for block in blocks]
dateTimess = [[datetime.strptime(col[5], '%Y-%m-%d %H:%M:%S') for col in block] for block in blocks]
timess = [[(t1-t).total_seconds() for t,t1 in zip(times[:-1],times[1:])] + [3.] for times in dateTimess]
delta = []

#average speeds
for speeds, times in zip(speedss, timess):
	try:
		delta.append(str(np.dot(np.array(speeds),np.array(times))/float(sum(times))))
	except:
		pass
print '\n'.join(delta)

