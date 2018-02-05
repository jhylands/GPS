class Trip:

	def __init__(self,tripArray):
		self.speeds = [point[2] for point in trip]
		self.times = [point[3] for point in trip]
		self.modeID = trip[0][1]