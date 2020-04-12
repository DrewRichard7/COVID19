from matplotlib import pyplot as plt
import numpy as np
import pandas as pd
from matplotlib.widgets import Cursor

UScountydata = pd.read_csv('nytimesCOVID/covid-19-data/us-counties.csv')
# print(UScountydata)
tndata_df = UScountydata[UScountydata['state'] == 'Tennessee'] # Getting Tennessee Data
# print(tndata_df)
hotcounties = ['Williamson','Davidson','Shelby','Unknown','Sumner','Rutherford','Knox','Hamilton','Robertson','Wilson','Putnam','Tipton','Washington']
coloring = ['#FF3333','#FF9933','#FFDD33','#99FF33','#33FFDD','#3333FF','#BB33FF','#FF33DD','#650909','#896603','#258903','#036E89','#3A0389']

i = 1
fig = plt.figure()
ax = fig.add_subplot(111)

for countyname in hotcounties:
    county_df = tndata_df[tndata_df['county'] == countyname]
    ax.plot(county_df['date'],county_df['cases'],color = coloring[i-1])
    # print(county_df)
    i+=1
    

cursor = Cursor(ax, useblit=True, color = 'red', linewidth = 2)
plt.legend(hotcounties, loc = 'upper left', fontsize = 'small',ncol = 2)
plt.xticks(rotation=90)
plt.show()
