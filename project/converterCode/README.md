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

What I'm currently working on is the problem of what data to transfure over.
--modify T2json 
--tripID: [points...]
--[tripID,pointID,speed,time]
The featureSet class want to take things as input speed array, time array

