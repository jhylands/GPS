function plotsomeconf(targetsVector,outputsVector,i,asize)
    f = figure;
    targets = zeros(4,asize);
    outputs = zeros(4,asize);
    targetsIdx = sub2ind(size(targets), targetsVector, 1:asize);
    outputsIdx = sub2ind(size(outputs), outputsVector, 1:asize);
    targets(targetsIdx) = 1;
    outputs(outputsIdx) = 1;
    % Plot the confusion matrix for a 3-class problem
    plotconfusion(targets,outputs);
    h = gca;
    label = {'Ride','Run','Walk','Motor',''};
    h.XTickLabel = label;
    h.YTickLabel = label;
    h.YTickLabelRotation = 90;
    saveas(h,strcat('testConf-',num2str(i),'-',num2str(asize),'.png') );
end