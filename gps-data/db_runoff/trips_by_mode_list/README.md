# Modes by modelist

This folder contains the csv resulting from:
'''
SELECT Trips2.TripID,PointID,gpsspeed,time_local from Trips2,Points2where Trips2.TripID=Points2.TripID and Trips2.travelmodelist="1" ORDERBY time_local
'''

with different travelmodelist indecies
