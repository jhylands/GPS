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
Runs = [Runs Runs(:,1)];%bassically
Walks = Walks(:,1:120);
Car = Car(:,1:440);
Passenger = Passenger(:,1:20);
%bus is alread divisible by 10
Motorised = [Car Passenger Bus];
 
%setup training boxes
training = ones(20,1080);  
RideIndx = 1:486;
training(1,RideIndx) = 2;
RunIndx = 487:540;
training(1,RunIndx) = 5;
WalkIndx = 541:648;
training(1,WalkIndx) = 1;
MotorIndx = 649:1080;
training(1,MotorIndx) = 3;

testing = ones(20,119);
testing(1,1:54) = 2;
testing(1,55:60) = 5;
testing(1,61:72) = 1;
testing(1,73:120) = 3;

%get cross validation scripts (slow, could do with opermising)
[I,Iv] = crossVal(Rides');
[U,Uv] = crossVal(Runs');
[W,Wv] = crossVal(Walks');
[M,Mv] = crossVal(Motorised');

%creating and training the network (10 cross validations)
for i = 1:10
    
    training(2:20,RideIndx) = I{i}'; %486 items
    training(2:20,RunIndx) = U{i}'; %56 items
    training(2:20,WalkIndx)= W{i}'; %108 items
    training(2:20,MotorIndx) = M{i}'; %423 items

    testing(2:20,1:54) = Iv{i}';
    testing(2:20,55:60) = Uv{i}';
    testing(2:20,61:72) = Wv{i}';
    testing(2:20,73:120) = Mv{i}';

    net{i} = selforgmap([8 8]);
    net{i} = train(net{i},training(2:20,:));
    
    %images for each of the networks
    %outputting the planes
    f = figure;
    plotsomplanes(net{i});
    filename = strcat('plotsomplanes', num2str(i), '.png');
    saveas(f,filename);

    %plotsomhits of network i
    plotsomehits(net{i},training(2:20,:),'training',i);
    plotsomehits(net{i},training(2:20,RideIndx),'Rides',i);
    plotsomehits(net{i},training(2:20,RunIndx),'Runs',i);
    plotsomehits(net{i},training(2:20,WalkIndx),'Walks',i);
    plotsomehits(net{i},training(2:20,MotorIndx),'Motorised',i);

    plotsomehits(net{i},testing(2:20,:),'testing',i);
    plotsomehits(net{i},testing(2:20,1:54),'Rides',i);
    plotsomehits(net{i},testing(2:20,55:60),'Runs',i);
    plotsomehits(net{i},testing(2:20,61:72),'Walks',i);
    plotsomehits(net{i},testing(2:20,73:120),'Motorised',i);
    %a results file to be worked with 
end
%copy of the networks saved

save('networks','net')



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



