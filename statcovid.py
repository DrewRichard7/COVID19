# Coronavirus statistical analysis - Started March 12 2013 at 10:29 PM
from matplotlib import pyplot as plt
import numpy as np
import pandas as pd
from matplotlib.widgets import MultiCursor
import statistics
import scipy.stats 
try:
    df = pd.read_csv(
        'COVID-19/who_covid_19_situation_reports/who_covid_19_sit_rep_time_series/who_covid_19_sit_rep_time_series.csv', index_col=0)
except:
    print("Dataset not available, please clone repo listed in README")
    exit()

df.set_index("Country/Region", inplace=True)
dates = df.iloc[42, 3:46]
print(dates)
fig = plt.figure()
plt.plot(dates)
plt.xticks(rotation=45)
plt.show()
