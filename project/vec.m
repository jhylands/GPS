theVectors = vec2ind(net(training(2:20,:)));
acc="";
for box = [1:64]
    checkBox = ones(1,1223)*box;
    routeIndecies = find(checkBox==theVectors);
    allOneString = sprintf('%.0f,' , routeIndecies);
    acc = strcat(acc ,"\n" ,allOneString(1:end-1));% strip final comma    
end
