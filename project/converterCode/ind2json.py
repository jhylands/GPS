import sys
indFile = sys.argv[1]
with open(indFile,'r') as f:
    data = f.read().split('\n')
outFile = sys.argv[2]
with open(outFile,'w+') as f:
    f.write('[' + ',\n'.join(['[%s]'%d for d in data]) + ']')
print 'fin'
