function plotsomehits(network,data,name,index)
    %set(0,'DefaultFigureVisible','off')
    f = figure;
    plotsomhits(network,data)
    filename = strcat('plotsomhits-', name , '-',num2str(index), '.png');
    saveas(f,filename);
    %set(0,'DefaultFigureVisible','on')
end
