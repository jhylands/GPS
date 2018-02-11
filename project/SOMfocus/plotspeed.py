#This file take file in J
import sys,json
import matplotlib
matplotlib.use('Agg')
from matplotlib import pyplot as plt
name='fig'

#arg1 being the file
strFile = sys.argv[1]
name = sys.argv[2]
with open(strFile ,'r') as f:
	readFile = json.loads(f.read())

V = [v for v,t in readfile]
T = [t for v,t in readfile]

plt.plot(range(1,10))
plt.savefig(name + '.png')



