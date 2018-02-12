#Test featureSet class

import json
from FeatureSet import FeatureSet
#load data for test
with open('test.json','r') as f:
    data = json.loads(f.read())

#extract the time data from the json file
T = FeatureSet.getTime(data)
print 'Time extraction function complete'
#the conversion shouldn't change the ammount of data 
assert(len(T)==len(data))
#the conversion shouldn't change the length of the individual data elements 
assert(True)
#the elements should be of type date 
assert(True)

#extract the speed data from the json file 
d1x = FeatureSet.getSpeed(data)
print 'Speed extraction function complete'
#the conversion shouldn't change the length of the individual data elemnts 

#create an instance of the featureset class
fs = FeatureSet(d1x,1,T)
print 'FeatureSet instance produced'

#Add mean to the set of columns
fs.mean(1)
print 'Mean created'

print len(fs.retrive()[0])
