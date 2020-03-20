# Coronavirus statistical analysis - Started March 12 2013 at 10:29 PM
# Scratch code file

import pandas as pd
from matplotlib import pyplot as plt

try:
    confirmed_df = pd.read_csv(
        'COVID-19/csse_covid_19_data/csse_covid_19_time_series/time_series_19-covid-Confirmed.csv')
except IOError:
    print("Dataset not available, please clone repo listed in README")
    exit()

df = confirmed_df.drop(columns=['Lat', 'Long'])
df_US = df[df['Country/Region'] == 'US']
print(type(df_US))
