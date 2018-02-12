#trips to json 
#This python file take the single mode trips csv files and makes 2D array of them
import sys,json

def toInt(S):
	return int(S.replace('"',''))
def  toString(S):
	return S.replace('"','')
def toFloat(S):
	return float(S.replace('"',''))
def point2point(point):
	return [toInt(point[0]),toInt(point[1]),toFloat(point[2]),toString(point[3])]

#get the filename of the input file
name = sys.argv[1]
with open(name,'r') as f:
    file = [a.split(',') for a in f.read().splitlines()]

#create a dictionary for keys
trips = {}
for row in file:
    if row[0] in trips:
	trips[row[0]].append(point2point(row))
    else:
	trips.update({row[0]:[point2point(row)]})

#get the filename of the output file 
name = sys.argv[2]
with open(name,'w+') as f:
    f.write(json.dumps(trips))

print 'fin'
