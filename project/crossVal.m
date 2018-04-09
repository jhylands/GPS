function [M,Mv] = crossVal(vector)
        %ungeneralising
        ten = [1,2,3,4,5,6,7,8,9,10];
        ind = ten * size(vector,1)/10
        M{1} = vector(ind(1):end,:);
        for x=2:9
            M{x} = [vector(1:ind(x-1),:); vector(ind(x)+1:end,:)];
        end 
        M{10} = vector(1:ind(9)+1,:);

        Mv{1} = vector(1:ind(1),:);
        for x=2:10                                                           
            Mv{x} = vector(ind(x-1):ind(x),:);
        end                                                                  
end 
