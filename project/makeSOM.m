set(0, 'defaultFigureRenderer', 'painters')
load('all.m' ,'-mat');
net = selforgmap([8 8]);
net = train(net,M(2:20,:));
f = figure;
plotsomeplanes(net);
saveas(f,'img.png');


Rides = ('../gps-data/FormJ1.1/ride.json.csv',1);
Runs = csvread('../gps-data/FormJ1.1/run.json.csv',1);
Walks = csvread('../gps-data/FormJ1.1/walk.json.csv',1);
Car = csvread('../gps-data/FormJ1.1/car.json.csv',1);
Passenger = csvread('../gps-data/FormJ1.1/Passenger.json.csv',1);
Bus = csvread('../gps-data/FormJ1.1/bus.json.csv',1);
M = ones(20,size(Rides,1)+size(Bus,1)+size(Runs,1)+size(Walks,1)+size(Car,1)+size(Passenger,1));
M(2:20,1:546) = Rides';
M(2:20,547:605) = Runs';
M(2:20,606:731)=Walks';
M(2:20,732:1179) = Car';
M(2:20,1180:1203) = Passenger';
M(2:20,1204:1223) =Bus'
M(1,1:546) = 2;
M(1,547:605) = 5;
M(1,606:731) = 1;
M(1,732:1179) = 3;
M(1,1180:1203) = 4;
M(1,1204:1223) = 7;

