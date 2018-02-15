#import the file                     
import matplotlib
matplotlib.use('Agg')
import sys,json
from matplotlib import pyplot as plt
elm = sys.argv[1]
name = sys.argv[2]
sys.path.append('../converterCode/')
from FeatureSet import FeatureSet
with open(name,'r') as f:
    trips = json.loads(f.read())
T = FeatureSet.getTime(trips)
dnx,n = FeatureSet.getdnx(trips)
fs = FeatureSet(dnx,n,T)
d1x = fs.dOFx[1]
#lets look deaper into this walking
plot = [a for a in d1x[int(elm)]]
#print plot
plt.plot(plot)
name = sys.argv[3]
plt.savefig(name) 
