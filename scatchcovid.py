# Coronavirus statistical analysis - Started March 12 2013 at 10:29 PM
# from matplotlib import pyplot as plt
# import numpy as np
import pandas as pd
# try:
#     df = pd.read_csv(
#         'COVID-19/who_covid_19_situation_reports/\
# who_covid_19_sit_rep_time_series\/who_covid_19_sit_rep_time_series.csv',\
#  index_col=0)
# except:
#     print("Dataset not available, please clone repo listed in README")
#     exit()

# import datetime
# import geopandas as gpd

# time_format = "COVID-19/csse_covid_19_data/csse_covid_19_daily_reports\
# /%m-%d-%Y.csv"
# current_date = datetime.date(2020, 3, 1)
# import os
# import fnmatch

# for file_name in os.listdir('COVID-19/csse_covid_19_data/\
# csse_covid_19_daily_reports'):
#     if fnmatch.fnmatch(file_name, '*.csv'):
#         print(file_name)
try:
    confirmeddf = pd.read_csv(
        'COVID-19/csse_covid_19_data/csse_covid_19_time_series/time_series_19-covid-Confirmed.csv', index_col=0)
except:
    print("Dataset not available, please clone repo listed in README")
exit()
try:
        deathsdf = pd.read_csv(
            'COVID-19/csse_covid_19_data/csse_covid_19_time_series/time_series_19-covid-Deaths.csv', index_col=0)
except:
    print("Dataset not available, please clone repo listed in README")
exit()
try:
        recovereddf = pd.read_csv(
            'COVID-19/csse_covid_19_data/csse_covid_19_time_series/time_series_19-covid-Recovered.csv', index_col=0)
except:
        print("Dataset not available, please clone repo listed in README")
exit()

confirmeddf.set_index("Country/Region", inplace=True)
# usadates = df.iloc[42, 3:46].reset_index()
confimredx = usadates['index']
print(confimredx)
# confirmedy = usadates["United States of America"]
# fig = plt.figure()
# plt.subplot(211)
# plt.title('United States Growth')
# plt.scatter(usax, usay)
# plt.xticks(np.arange(0, len(usax), step=7), rotation=45)
# plt.show()
