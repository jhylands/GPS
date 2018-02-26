class FormJ():
    def __init__(self,fileName):
	with open(fileName,'r') as f:
	    trips = json.loads(f.read())

