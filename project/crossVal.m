function [training,testing] = crossVal(n,x,vector)
    training  = [vector(1:n*(x-1)); vector(n*x:end)];
    testing = vector(n*(x-1):n*x);
end

%ungeneralising
MororisedIndecies = ten * 48

MororisedIndecies =

    48    96   144   192   240   288   336   384   432   480

M{1} = Motorised(49:end,:);                     
M{2} = [Motorised(1:48,:); Motorised(97:end,:)];
M{3} = [Motorised(1:96,:); Motorised(145:end,:)];
M{4} = [Motorised(1:144,:); Motorised(193:end,:)];
M{5} = [Motorised(1:192,:); Motorised(241:end,:)];
M{6} = [Motorised(1:240,:); Motorised(289:end,:)];
M{7} = [Motorised(1:288,:); Motorised(337:end,:)];
M{8} = [Motorised(1:336,:); Motorised(385:end,:)];
M{9} = [Motorised(1:384,:); Motorised(433:end,:)];
M{10} = Motorised(1:432,:);                        

Mv{1} = Motorised(1:48,:);
for x=2:10                                                           
    Mv{x} = Motorised(MororisedIndecies(x-1):MororisedIndecies(x),:);
end                                                                  
 
