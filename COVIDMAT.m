close all;clc;clear all

time = clock;
currentmonth = sprintf('%02d',time(2));
currentday = num2str(time(3)-2);
currentyear = num2str(time(1));

currentdata = readmatrix('COVID-19/csse_covid_19_data/csse_covid_19_time_series/time_series_19-covid-Confirmed.csv');

% countUS = count(currentdata.textdata,'US');
% amountofUS = sum(countUS);

% if currentdata.textdata(:,2) == string(US)
%    for i = 1:amountofUS(2)
%        confirmedcases = sum(currentdata.data(,:
%    end
%    
% end
% a = 0
% for i = 1:amountofUS
%     if countUS == 1
%         a = a + currentdata.data(countUS(
        
        
        
        