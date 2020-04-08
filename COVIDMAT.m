close all;clc;clear all

time = clock;
currentmonth = sprintf('%02d',time(2));
currentday = num2str(time(3));
currentyear = num2str(time(1));
dayssince122 = str2double(currentday) + 38;

currentdata = readtable('COVID-19/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv');
globalreadcases = readmatrix('COVID-19/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv');
globalreaddeaths = readmatrix('COVID-19/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_deaths_global.csv');
globalreadrecovered = readmatrix('COVID-19/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_recovered_global.csv');

figure(1)
xaxislimit = 120;
subplot(2,1,1);

% Plot Global Cases
A = nansum(globalreadcases);
globalcases(1,:) = A(5:1:length(A));
x = 0:(length(globalreadcases(1,:))-5);
plot(x,globalcases(1,:))
ylabel('Numbers of People')
xlabel('Days since 01/22/20')
ax = gca;
ax.YAxis.Exponent = 0;
title('Global COVID-19 Data')
hold on

% Plot Global Recovered
B = nansum(globalreadrecovered);
globalrecovered(1,:) = B(5:1:length(B));
y = 0:(length(globalreadrecovered(1,:))-5);
plot(y,globalrecovered(1,:))
xlim([0 xaxislimit]);
hold on

% Plot Global Deaths
C = nansum(globalreaddeaths);
globaldeaths(1,:) = C(5:1:length(C));
z = 0:(length(globalreaddeaths(1,:))-5);
plot(z,globaldeaths(1,:))
xlim([0 xaxislimit]);
hold on
% curve fitting 

casesofCOVID19 = globalcases(1,:);
totalcasestoday = globalcases(length(globalcases));
totalrecoveredtoday = globalrecovered(length(globalrecovered));
totaldeathstoday = globaldeaths(length(globaldeaths));

text(5,1000000,strcat('Total Cases as of Today:  ',string(totalcasestoday),''))
text(5,750000,strcat('Total Recovered as of Today:  ',string(totalrecoveredtoday),''))
text(5,500000,strcat('Total Deaths as of Today:  ',string(totaldeathstoday),''))

d = .117;
popsize = 3000000;
DaysIntoTheFuture = 5;
N = zeros(length(x)+DaysIntoTheFuture);
for i = 1:(length(x)+DaysIntoTheFuture)
    N(1) = 555;
    N(i+1) = d.*(1-(N(i)./popsize)).*N(i) + N(i);
    plot(i,N(i+1),'.')
end


 a =   3.006e+07;
 b =      0.0914;
 c =   1.938e+04;

p = @(r) a/(1 + c*exp(-b*r));

% fplot(p,[0 300])

% logistic curve with inflection point on 3/17/20 (x,y) = (55,197100)
% f = K/(1+Z*exp(-k*t)) 
% where inflection point is (ln(Z)/k,K/2)
% and Z = K-f(0)/f(0) 
% assuming f(0) = 1

syms t k K f Z

% inflectionpoint data (x,y)
inflectionday = 69; % measured in days from 1/22/20
inflectioncases = 857000; % confirmed cases from that day
initialcases = 555; % confirmed cases on 1/22/20 // Do not change for now 

K = 2*inflectioncases;
Z = 2*inflectioncases - initialcases;
k = log(Z)./inflectionday;
f = @(t) K./(1+Z.*exp(-k.*t));

% fplot(f,[0 120])
finalday = 1.5*inflectionday;
finalcases = K;
legend('Confirmed Cases','Recovered','Deaths','Logistic Curve (Projected Growth)','Location','best')

subplot(2,1,2)
slope = zeros(1,length(x));
for i = 1:(length(x)-1)
   slope(1,i) = globalcases(1,i+1)-globalcases(1,i);
end
plot(x(1:length(x)-1),slope(1:length(x)-1))
ylabel('New Patients per Day')
xlabel('Days since 01/22/20')
title('Slope Analysis')
xlim([0 xaxislimit]);
legend('Number of New Cases Reported','Location','best')


        