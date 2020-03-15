close all;clc
time = clock;
currentmonth = fprintf('%02d',time(2))
currentday = time(3)-1;
currentyear = time(1);

for year = 2020:currentyear
    for month = 01:currentmonth
        disp(month)
%         if month == 04 || month == 06 || month == 09 || month == 11
%            for day = 01:30
%                currentdata = importdata(strcat('COVID-19/csse_covid_19_data/csse_covid_19_daily_reports/',string(month),'-',string(day),'-',string(year),'.csv'));
%            end 
%         elseif month == 02
%            for day = 01:29
%                currentdata = importdata(strcat('COVID-19/csse_covid_19_data/csse_covid_19_daily_reports/',string(month),'-',string(day),'-',string(year),'.csv'));
%            end
%         elseif month == 01
%            for day = 22:31
%                currentdata = importdata(strcat('COVID-19/csse_covid_19_data/csse_covid_19_daily_reports/',string(month),'-',string(day),'-',string(year),'.csv'));
%            end
%         else 
%            for day = 01:31
%                currentdata = importdata(strcat('COVID-19/csse_covid_19_data/csse_covid_19_daily_reports/',string(month),'-',string(day),'-',string(year),'.csv'));
%            end
%         if month == currentmonth
%            for day = 01:currentday
%                currentdata = importdata(strcat('COVID-19/csse_covid_19_data/csse_covid_19_daily_reports/',string(month),'-',string(day),'-',string(year),'.csv'));
%            end
%         end
        

% readmatrix uses just the numbers whereas importdata gives two files with
% numbers in a matrix (.data) and then names as a text file (.textdata)
% currentdata = readmatrix(strcat('/Users/aclayrichard/Desktop/lab/COVID19/COVID-19/csse_covid_19_data/csse_covid_19_daily_reports/0',string(month),'-',string(day),'-',string(year),'.csv'))
   
        % end 
    end
end 