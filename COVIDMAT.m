close all;clc
format long g
time = clock;
month = time(2);
day = time(3)-2;
year = time(1);

currentdata = importdata(strcat('COVID-19/csse_covid_19_data/csse_covid_19_daily_reports/0',string(month),'-',string(day),'-',string(year),'.csv'));

% readmatrix uses just the numbers whereas importdata gives two files with
% numbers in a matrix (.data) and then names as a text file (.textdata)
% currentdata = readmatrix(strcat('/Users/aclayrichard/Desktop/lab/COVID19/COVID-19/csse_covid_19_data/csse_covid_19_daily_reports/0',string(month),'-',string(day),'-',string(year),'.csv'))