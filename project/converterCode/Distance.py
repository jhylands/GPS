
    

'''
python file to aid in the calculating of the derivitive of the file 
'''
class dif():
    @staticmethod
    def dtripdt(x,t):
	assert(not(isinstance(x[0],list)))
	print t[0]
	assert(not(isinstance(t[0],list)))

	if(isinstance(t[0],datetime)):
	    return [safeDiv((x2-x1),(t2-t1).total_seconds()) for x1,x2,t1,t2 in zip(x[:-1],x[1:],t[:-1],t[1:])]
	else:
	    return [(x2-x1)/t1.total_seconds() for x1,x2,t1,t2 in zip(x[:-1],x[1:],t[:-1],t[1:])]

    @staticmethod
    def dtripdt(dt):
	
    def pointDiff(x1,x2,t1,t2):
	#class to look at the times to make sure that it calculates it correctly
	#the two time types must be the same
	type(t1)==type(t2)
	#if they are of type timedelta use the first one 
	if type(t1)==type(datetime.timedelta):
	    t = t1.total_seconds()
	    return self.Diff(x1,x2,t)

	elif type(t1) == type(datetime.datetime):
	    t = self.getDelta(t1,t2)
	    return self.Diff(x1,x2,t)
	
    def __datetime__(t1,t2):
	
    def Diff(x1,x2,t):
	if(t<>0):
	    return (x2-x1)/t
	else:
	    print('zero delta error')
	    return (x2-x1)
