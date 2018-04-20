function plotsomehits(network,data,name,index)
    f = figure;
    plotsomhits(network,data)
    filename = strcat('plotsomhits-', name , '-',num2str(index), '.png');
    saveas(f,filename);
end
