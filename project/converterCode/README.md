# Converter Code

This folder contains the code to convert varius types of gps data into a form that can be used.

There are two formats that need to be converted to.

-The first is an intermediary JSON file which contains an array of trips, as an array.
--This is called J
-The second is a csv which contains the features of the trips as columns. In this file each row corresponds to a trip.
--This is called C

## Progression 

				    v:a
Database query -> CSV -> T2json -> json2Vec -> CSV

a: the desired vector is also an input to json2Vec

What I'm currently working on is being able to get the gpx file included in a natural way to the dataset.
I think I have managed to do that. However they take a long time to convert and the calculation has to be done on the pi due to the permisions required by the gpx file reading libary.
