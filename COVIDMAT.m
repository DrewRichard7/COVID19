close all;clc;clear all

time = clock;
currentmonth = sprintf('%02d',time(2));
currentday = num2str(time(3)-2);
currentyear = num2str(time(1));

currentdata = readtable('COVID-19/csse_covid_19_data/csse_covid_19_time_series/time_series_19-covid-Confirmed.csv');
globalreadcases = readmatrix('COVID-19/csse_covid_19_data/csse_covid_19_time_series/time_series_19-covid-Confirmed.csv');
globalreaddeaths = readmatrix('COVID-19/csse_covid_19_data/csse_covid_19_time_series/time_series_19-covid-Deaths.csv');
globalreadrecovered = readmatrix('COVID-19/csse_covid_19_data/csse_covid_19_time_series/time_series_19-covid-Recovered.csv');


% Plot Global Cases
A = nansum(globalreadcases);
globaldata(1,:) = A(5:1:length(A));
x = 0:(length(globalreadcases(1,:))-5);
plot(x,globaldata(1,:))
ylabel('Numbers of People')
xlabel('Days since 01/22/20')
ax = gca;
ax.YAxis.Exponent = 0;
title('Global COVID-19 Cases')
hold on

% Plot Global Deaths
B = nansum(globalreadrecovered);
globaldata(1,:) = B(5:1:length(B));
y = 0:(length(globalreadrecovered(1,:))-5);
plot(y,globaldata)
hold on

% Plot Global Recoveries
C = nansum(globalreaddeaths);
globaldata(1,:) = C(5:1:length(C));
z = 0:(length(globalreaddeaths(1,:))-5);
plot(z,globaldata(3,:))

% for curve fitting purposes as of 3/19/20 -> R-square = 0.9429
% lengthofA = 1:1:length(A);
casesofCOVID19 = globaldata(1,:);

a =    1.18e+09; 
b =   7.534e+04; 
c =      0.0452;
p = @(r) a./(1+b.*exp(-c.*r));

% fplot(p,[0 500])

% logistic curve with inflection point on 3/17/20 (x,y) = (55,197100)
% f = K/(1+A*exp(-k*t)) 
% where inflection point is (ln(A)/k,K/2)
% and A = K-f(0)/f(0) 
% assuming f(0) = 1

syms t k K f A

% inflectionpoint data (x,y)
inflectionday = 55; % measured in days from 1/22/20
inflectioncases = 197100; % confirmed cases from that day
initialcases = 555; % confirmed cases on 1/22/20 // Do not change for now 


K = 2*inflectioncases;
A = 2*inflectioncases - initialcases;
k = log(A)./inflectionday;
f = @(t) K./(1+A.*exp(-k.*t));

fplot(f,[0 120])
legend('Confirmed Cases','Recovered','Deaths','logistic curve','Location','best')


% Plot USA Data
% arraydata = table2cell(currentdata);
% 
% cell2mat(arraydata)


        
        
        
        