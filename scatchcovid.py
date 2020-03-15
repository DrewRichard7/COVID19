# Coronavirus statistical analysis - Started March 12 2013 at 10:29 PM
from matplotlib import pyplot as plt
import numpy as np
import pandas as pd
try:
    df = pd.read_csv(
        'COVID-19/who_covid_19_situation_reports/who_covid_19_sit_rep_time_series/who_covid_19_sit_rep_time_series.csv', index_col=0)
except:
    print("Dataset not available, please clone repo listed in README")
    exit()

import datetime
import geopandas as gpd

time_format = "COVID-19/csse_covid_19_data/csse_covid_19_daily_reports/%m-%d-%Y.csv"
current_date = datetime.date(2020, 3, 1)
