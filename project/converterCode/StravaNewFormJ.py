#This file is for the conversion of the FormJ1 to FormJ1.1
#This means that the points array goes from length two to length 4 but is standerdised
#This should reduce computational requirements on FeatureSet as the derivitives won't need to be calculated every time we load the file in.
import json,sys
from datetime import datetime,timedelta
#calculate the velocities for one trace
def velocitys(x,t):
    assert(isinstance(t[0],datetime))
    assert(isinstance(x[0],float))
    try:
        return [x1/(t2-t1).total_seconds() for x1,x2,t1,t2 in zip(x[:-1],x[1:],t[:-1],t[1:])]
    except ZeroDivisionError:
        for t1,t2 in zip(t[1:],t[:-1]):
	    print 'vel: '+str(t1) + str(t2) + str(t2-t1)

def accelerations(x,t):
    assert(isinstance(t[0],datetime))
    assert(isinstance(x[0],float))
    try:
        return [(x2-x1)/(t2-t1).total_seconds() for x1,x2,t1,t2 in zip(x[:-1],x[1:],t[:-1],t[1:])]
    except ZeroDivisionError:
        for t1,t2 in zip(t[1:],t[:-1]):
	    print 'acc:' + str(t1) + str(t2) + str(t2-t1)

name = sys.argv[1]
with open(name,'r') as f:
    data = json.loads(f.read())

#now we have the thrice nested array 
#calculate the derivitives
data2 = []
i =0
WO = 'Working on '
#create trip columns
for trip in data:
    print '-'*20
    print WO + " data element: " + str(i)
    print WO + 'distance'
    D = [d for d,t in trip]
    print D[0]
    print  WO + 'time'
    T = [datetime.strptime(t, '%Y-%m-%d %H:%M:%S') for d,t in trip]
    print T[0]
    print WO +'velocity'
    V = velocitys(D,T)
    V = V + [V[-1]]
    print V[0]
    print WO +'acceloration'
    A = accelerations(V,T)
    A = A + [A[-1]]
    print A[0]
    print WO +'trip composition'
    trip2 = [[d,v,a,t.strftime('%Y-%m-%d %H:%M:%S')] for d,v,a,t in zip(D,V,A,T)]
    data2.append(trip2)
    i+=1

#Velocity  = [ velocitys([d for d,t in trip] , [t for d,t in trip]) for trip in data]
#Make velocity the same length as distance 
#Velocity = Velocity + [Velocity[-1]]

#create acceloratin
#Acceloration = [accelerations(v,t) for v,(d,t) in zip(Velocity,data)
name = sys.argv[2]
with open(name,'w+') as f:
    f.write(json.dumps(data2))
print 'fin'
