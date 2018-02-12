M = csvread('../converterCode/out.csv',1);
f=figure;
scatter(M(:,1),M(:,2))
saveas(f,'scate.png')
exit()
