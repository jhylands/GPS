#import the file                     
import matplotlib
matplotlib.use('Agg')
import sys,json
from FeatureSet import FeatureSet
from matplotlib import pyplot as plt
name = sys.argv[1]
with open(name,'r') as f:
    trips = json.loads(f.read())
T = FeatureSet.getTime(trips)
d1x = FeatureSet.getSpeed(trips)

#lets look deaper into this walking
plot = [a for a in d1x[0]]
print plot
plt.plot(plot)
plt.savefig('out.png') 
