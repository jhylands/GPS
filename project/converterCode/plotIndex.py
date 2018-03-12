import matplotlib
matplotlib.use('Agg')
import sys,json
from matplotlib import pyplot as plt

def makeGraph(name,index):
    i = index
    #check range
    #Rides
    if index<547:
        #take the index as is from the file
        filename = '../gps-data/FormJ1.1/ride.json'
        index -=1
    #Runs
    elif index<606:
        filename = '../gps-data/FormJ1.1/run.json'
        index -=547
    #Walks
    elif index<732:
        filename = '../gps-data/FormJ1.1/walk.json'
        index -= 606
    #Car
    elif index<1180:
        filename = '../gps-data/FormJ1.1/car.json'
        index -=732
    #Passenger
    elif index<1204:
        filename = '../gps-data/FormJ1.1/Passenger.json'
        index -=1180
    #Bus
    elif index<1224:
        filename = '../gps-data/FormJ1.1/bus.json'
        index -=1204

    with open(filename,'r') as f:
        traces = json.loads(f.read())
    trace = traces[index]

    plt.plot([x[1] for x in trace])
    #name = sys.argv[2]
    plt.savefig(name + str(i) + '.png')
    plt.clf()

#We want to take as argument and index
#index file as input
indexfile = sys.argv[1]
indecies=[[] for i in range(0,64)]
with open(indexfile,'r') as f:
    basename = '../images/boxes/box'
    for i in range(0,64):
        print 'Status: ' + str(i)
        line = f.readline()[:-2]
        if line<>'':
            indecies[i] = [int(x) for x in line.split(',') if x<>'']
        else:
            indecies[i] =[]
        for index in indecies[i]:
            makeGraph(basename + str(i+1) + '/',index)

print 'fin'
