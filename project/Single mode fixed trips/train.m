net2 = selforgmap([8 8]);
net2 = train(net2,featureall(:,2:end)');
figure;plotsomhits(net2,featureSetBike(:,2:end)');
title('Bike');
figure;plotsomhits(net2,featureSetRun(:,2:end)')
title('Run');
figure;plotsomhits(net2,featureSet1(indCar,2:end)')
title('Car');
figure;plotsomhits(net2,featureSet1(indBus,2:end)')
title('Bus');
figure;plotsomhits(net2,featureSet1(indWalk,2:end)')
title('Walk');
figure;plotsomhits(net2,featureSet1(indPas,2:end)')
title('Passenger');
figure;plotsomhits(net2,featureall(:,2:end)')
title('All');
figure;plotsomplanes(net)
title('Which');