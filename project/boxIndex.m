%Finding out the index of a group
%vec = vec2ind(net(M(2:20,732:1179)));
%yeilds a number 1-64 which starts at the bottom left and goes right, then
%up a line (starting from the left again)
for box = ones(1,64)
    vec = vec2ind(net(M(2:20,:)));
    checkBox = ones(1,1223)*box;
    routeIndecies = find(checkBox);
    allOneString = sprintf('%.0f,' , routeIndecies);
    allOneString(1:end-1)% strip final comma    
end