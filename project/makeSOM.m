set(0, 'defaultFigureRenderer', 'painters')
%Does loading all not assume that they are already loaded
%load('all.m' ,'-mat');

%loading the feature space in
Rides = csvread('../gps-data/FormJ1.1/ride.json.csv',1);
Runs = csvread('../gps-data/FormJ1.1/run.json.csv',1);
Walks = csvread('../gps-data/FormJ1.1/walk.json.csv',1);
Car = csvread('../gps-data/FormJ1.1/car.json.csv',1);
Passenger = csvread('../gps-data/FormJ1.1/Passenger.json.csv',1);
Bus = csvread('../gps-data/FormJ1.1/bus.json.csv',1);
M = ones(20,size(Rides,1)+size(Bus,1)+size(Runs,1)+size(Walks,1)+size(Car,1)+size(Passenger,1));
M(2:20,1:546) = Rides';
M(2:20,547:605) = Runs';
M(2:20,606:731)= Walks';
M(2:20,732:1179) = Car';
M(2:20,1180:1203) = Passenger';
M(2:20,1204:1223) = Bus';
M(1,1:546) = 2;
M(1,547:605) = 5;
M(1,606:731) = 1;
M(1,732:1179) = 3;
M(1,1180:1203) = 4;
M(1,1204:1223) = 7;

%creating and training the network
net = selforgmap([8 8]);
net = train(net,M(2:20,:));

%outputting the planes
f = figure;
plotsomplanes(net);
saveas(f,'img.png');

%plot som hits for each group
%plotsomhits

%Finding out the index of a group
%vec = vec2ind(net(M(2:20,732:1179)));
%yeilds a number 1-64 which starts at the bottom left and goes right, then
%up a line (starting from the left again)
theVectors = vec2ind(net(M(2:20,:)));
acc="";
for box = [1:64]
    checkBox = ones(1,1223)*box;
    routeIndecies = find(checkBox==theVectors);
    allOneString = sprintf('%.0f,' , routeIndecies);
    acc = strcat(acc ,"\n" ,allOneString(1:end-1));% strip final comma    
end

fid = fopen('indecies.csv','wt');
fprintf(fid,acc);
fclose(fid);



