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
 
SOMD1=10;
SOMD2=3;

%get cross validation scripts (slow, could do with opermising)
[I,Iv] = crossVal(Rides');
[U,Uv] = crossVal(Runs');
[W,Wv] = crossVal(Walks');
[M,Mv] = crossVal(Motorised');
Pos = cell(1,10);
tst = cell(1,10);
a = cell(1,10);
b = cell(1,10);
targetsVector = cell(1:10);
targetsVector1 = cell(1:10);
outputsVector = cell(1:10);
outputsVector1 = cell(1:10);
%creating and training the network (10 cross validations)
parfor i = 1:10
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
    training(2:20,RideIndx) = I{i}'; %486 items
    training(2:20,RunIndx) = U{i}'; %56 items
    training(2:20,WalkIndx)= W{i}'; %108 items
    training(2:20,MotorIndx) = M{i}'; %432 items

    testing(2:20,1:54) = Iv{i}';
    testing(2:20,55:60) = Uv{i}';
    testing(2:20,61:72) = Wv{i}';
    testing(2:20,73:120) = Mv{i}';

    net{i} = selforgmap([SOMD1 SOMD2]);
    net{i} = train(net{i},training(2:20,:));
    
    %images for each of the networks
    %outputting the planes
    f = figure;
    plotsomplanes(net{i});
    filename = strcat('plotsomplanes', num2str(i), '.png');
    saveas(f,filename);

    %plotsomhits of network i training
    plotsomehits(net{i},training(2:20,:),'training',i);
    plotsomehits(net{i},training(2:20,RideIndx),'Rides',i);
    plotsomehits(net{i},training(2:20,RunIndx),'Runs',i);
    plotsomehits(net{i},training(2:20,WalkIndx),'Walks',i);
    plotsomehits(net{i},training(2:20,MotorIndx),'Motorised',i);
    %same for testing
    plotsomehits(net{i},testing(2:20,:),'testing',i);
    plotsomehits(net{i},testing(2:20,1:54),'Rides',i);
    plotsomehits(net{i},testing(2:20,55:60),'Runs',i);
    plotsomehits(net{i},testing(2:20,61:72),'Walks',i);
    plotsomehits(net{i},testing(2:20,73:120),'Motorised',i);
    
    %a results file to be worked with 
    %Finding out the index of a group
    %vec = vec2ind(net(training(2:20,732:1179)));
    %yeilds a number 1-64 which starts at the bottom left and goes right, then
    %up a line (starting from the left again)
    Pos{i}{1} = vec2ind(net{i}(training(2:20,RideIndx)));
    Pos{i}{2} = vec2ind(net{i}(training(2:20,RunIndx)));
    Pos{i}{3} = vec2ind(net{i}(training(2:20,WalkIndx)));
    Pos{i}{4} = vec2ind(net{i}(training(2:20,MotorIndx)));
    tst{i}{1} = vec2ind(net{i}(testing(2:20,1:54)));
    tst{i}{2} = vec2ind(net{i}(testing(2:20,55:60)));
    tst{i}{3} = vec2ind(net{i}(testing(2:20,61:72)));
    tst{i}{4} = vec2ind(net{i}(testing(2:20,73:120)));

    
    %we have a list of indecies
    for v = 1:4
        for somclass=1:SOMD1*SOMD2
            a{i}{somclass}(v) = sum(Pos{i}{v}==somclass);
        end
    end
    for somclass =1:SOMD1*SOMD2
        [MaxSOMCLASSTHING,maxIndex] = max(a{i}{somclass});
        b{i}{somclass} = maxIndex;
    end
    %b{i} contains the classes of the SOM
    
    %test confusion
    targetsVector{i}(1:54) = 1;
    targetsVector{i}(55:60) = 2;
    targetsVector{i}(61:72)=3;
    targetsVector{i}(73:120)=4;
    outputsVector{i} = [b{i}{tst{i}{1}} b{i}{tst{i}{2}} b{i}{tst{i}{3}} b{i}{tst{i}{4}}];
    plotsomeconf(targetsVector{i},outputsVector{i},i,120)
    
    %train confusion
    targetsVector1{i}(RideIndx) = 1;
    targetsVector1{i}(RunIndx) = 2;
    targetsVector1{i}(WalkIndx)=3;
    targetsVector1{i}(MotorIndx)=4;
    outputsVector1{i} = [b{i}{Pos{i}{1}} b{i}{Pos{i}{2}} b{i}{Pos{i}{3}} b{i}{Pos{i}{4}}];
    plotsomeconf(targetsVector1{i},outputsVector1{i},i,1080)
    
end
%copy of the networks saved

save('networks','net')



'fin'


