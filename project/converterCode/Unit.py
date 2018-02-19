class Unit(Enum):

'''
X
This is the interface for a class which is a derivative of position with respect to time
'''
class X(Unit):
    def toSi(raw,unit):

    def __init__(self,raw,unit):
	self.raw = raw
	self.si = self.toSi(raw,unit)

'''
Class to manage sets of derivitives of position. 
'''
class Xset():
    def __init__(self,arrDistances):
	#keep an array of the individual X elements
	self.set = arrDistances
	#set the derivitive to 0 to indicate this class 
	#is starting as a distance set
	self.derivitive = 0
    def __getitem__(self,key):
	return self.set[key]
    def __len__(self):
	return len(self.set)

    def __eq__(self,comparison):
	return self.set==comparison.set and self.derivitive==comparison.derivative
    def __setitem__(self,key, value):
	if(not instanceof(value,X): raise TypeError
	try:
	    self.set[key] = value
	catch KeyError:
		raise KeyError



'''
This is a distance class managing elements of distance 
'''
class Distance(X):
    @abstract
    def toSi(self):
	return self.value * self.CONV

    def __init__(self,value):
	self.value=value

class Meter(Distance):
    self.CONV = 1

class Mile(Distance):
    self.CONV = 1609.34

class Velocity(X):
    def __init__(self,distance,time):
	assert(type(distance) is Distance)
	assert(type(time) is DateTime)
	self.DISTNCE= distance
	self.TIME = time

class Acceleration(X):
    #Enforce that time is symetric 
    #It must be a single ammount sqared and not, for example, per hours, per second.
    def __init__(self,distance,time):
	assert(type(distance) is Distance)
	assert((time) is DateTime)
	self.DISTNCE= distance
	self.TIME = time
