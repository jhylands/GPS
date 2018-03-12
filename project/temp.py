
def tadd(a,b):
    a1,a2 = a
    b1,b2 = b
    return (a1+b1,a2+b2)

def tmul(a,b):
    a1,a2 = a
    return (a1*b,a2*b)

def flatten(tupleList):
    if tupleList == []:
        return []
    else:
        a,b = tupleList[0]
        return [a,b] + flatten(tupleList[1:])

right = (428-309,0)
down_right = (427-368,233-130)
down = (0,205)
A=[(368,130),(309,164),(309,233),(368,266),(428,233),(428,164)] 

toprow = [[tadd(a,tmul(right,n)) for a in A] for n in range(0,8)]
oddrows = [ [ [tadd(x,tmul(down,n)) for x in X] for X in toprow] for n in range(0,4)]
downLeft = (309-368,233-130)
secondLeftMost = [tadd(a,downLeft) for a in A]
secondrow = [[tadd(a,tmul(right,n)) for a in secondLeftMost] for n in range(0,8)]
evenrows = [ [ [tadd(x,tmul(down,n)) for x in X] for X in secondrow] for n in range(0,4)]
allrows = oddrows+evenrows
allrows[::2] = oddrows
allrows[1::2] = evenrows
allrows.reverse()
#print allrows
allCells = [cell  for row in allrows for cell in row]
acc = ""
for cell,i in zip(allCells,xrange(0,len(allCells))):
    coords = ','.join(map(str,flatten(cell)))
    acc = acc + '<area alt="%d" title="" href="#%d" onclick="showCell(%d)" shape="poly" coords="%s" />\n' % (i,i,i,coords)

with open('som.html','w') as f:
    f.write('<h1>SOM Map</h1>\n<img src="../images/allHits.png" alt="" usemap="#Map" />\n<map name="Map" id="Map">')
    f.write(acc)
    f.write('</map>')
