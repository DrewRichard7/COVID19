close all;clc;clear all

time = clock;
currentmonth = sprintf('%02d',time(2));
currentday = num2str(time(3)-2);
currentyear = num2str(time(1));

globalread = readmatrix('COVID-19/csse_covid_19_data/csse_covid_19_time_series/time_series_19-covid-Confirmed.csv');
currentdata = readtable('COVID-19/csse_covid_19_data/csse_covid_19_time_series/time_series_19-covid-Confirmed.csv');


A = nansum(globalread);
globaldata(1,:) = A(5:1:length(A));
x = 0:(length(globalread(1,:))-5);
plot(x,globaldata)
ylabel('Confirmed Cases')
xlabel('Days since 01/22/20')
title('Global COVID-19 Cases')




% arraydata = table2cell(currentdata);
% 
% cell2mat(arraydata)


        
        
        
        