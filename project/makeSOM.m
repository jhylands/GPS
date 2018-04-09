set(0, 'defaultFigureRenderer', 'painters')
%Does loading all not assume that they are already loaded
%load('all.m' ,'-mat');

%loading the feature space in
Rides = csvread('../gps-data/FormJ1.1/ride.json.csv',1)';
Runs = csvread('../gps-data/FormJ1.1/run.json.csv',1)';
Walks = csvread('../gps-data/FormJ1.1/walk.json.csv',1)';
Car = csvread('../gps-data/FormJ1.1/car.json.csv',1)';
Passenger = csvread('../gps-data/FormJ1.1/Passenger.json.csv',1)';
Bus = csvread('../gps-data/FormJ1.1/bus.json.csv',1)';

%fit to 10 fold
Rides = Rides(:,1:540);
Runs = [Runs; Runs(:,1)]%bassically
Walks = Walks(:,1:120);
Car = Car(:,1:440);
Passenger = Passenger(:,1:20);
%bus is alread divisible by 10
Motorised = [Car; Passenger; Bus];
 
%setup training boxes
training = ones(20,1071); %1071 from paper calulation 
training(1,1:486) = 2;
training(1,487:540) = 5;
training(1,541:648) = 1;
training(1,649:1071) = 3;

%creating and training the network
for i = 1:5
    training(2:20,1:486) = Rides';
    training(2:20,487:540) = Runs';
    training(2:20,541:648)= Walks';
    training(2:20,649:1071) = Motorised';
    net{i} = selforgmap([8 8]);
    net{i} = train(net,training);
end


%outputting the planes
f = figure;
plotsomplanes(net);
saveas(f,'img.png');

%plot som hits for each group
%plotsomhits

%Finding out the index of a group
%vec = vec2ind(net(training(2:20,732:1179)));
%yeilds a number 1-64 which starts at the bottom left and goes right, then
%up a line (starting from the left again)
theVectors = vec2ind(net(training(2:20,:)));
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



