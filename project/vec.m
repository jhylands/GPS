%theVectors = vec2ind(net(training(2:20,:)));
acc="";
for box = [1:30]
    checkBox = ones(1,size(theVectors,2))*box;
    routeIndecies = find(checkBox==theVectors);
    box
    length(routeIndecies)
    allOneString = sprintf('%.0f,' , routeIndecies)
    acc = strcat(acc ,"\n" ,allOneString(1:end-1));% strip final comma    
end
