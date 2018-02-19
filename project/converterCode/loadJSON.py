
class JLoader():
#for both the time and speed feilds should do a type check to make sure the 
#structure of the array is what you think it is
    #get the time fields from the data 
    @staticmethod
    def getTime(data):
	if isinstance(data, dict):
	    assert(reduce(AND,[[len(x)==4 for x in trip] for trip in data.iteritems()]))
	    return [[datetime.strptime(t, '%Y-%m-%d %H:%M:%S') for TripID,PointID,v,t in trip] for key,trip in data.iteritems()]
	else:
	    assert(reduce(AND,[[len(x)==2 for x in trip] for trip in data]))
	    #some datetime from seconds
	    #return [[timedelta(0,point[1]) for point in trip if isinstance(point[1],float)] for trip in data]
	    return [[datetime.strptime(t,'%Y-%m-%d %H:%M:%S') for x,t in trip] for trip in data]
 
    #get the posion based data fields from the data 
    @staticmethod
    def getdnx(data):
	if isinstance(data, dict):
	    assert(reduce(AND,[[len(x)==4 for x in trip] for trip in data.iteritems()]))
	    return [[v for TripID,PointID,v,t in trip] for key,trip in data.iteritems()],1
	else:
	    assert(reduce(AND,[[len(x)==2 for x in trip] for trip in data]))
	    #some distances
	    return [[x for x,t in trip]  for trip in data],0

