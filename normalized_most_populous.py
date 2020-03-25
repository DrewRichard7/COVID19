
# NEEDS READDRESSING, FILE INPUT NAME/PATH

import pandas as pd
import matplotlib.pyplot as plt

path = '''COVID-19/csse_covid_19_data/csse_covid_19_time_series/\
time_series_covid19_confirmed_global.csv'''
try:
    covid19_df = pd.read_csv(path)
except IOError as e:
    print(e)
    exit()

url = 'https://www.worldometers.info/world-population/population-by-country/'
try:
    # pop_list = pd.read_html(url, attrs={'class': 'table'})
    # pop_list[0].to_csv('populations.csv')
    pop_list = pd.read_csv('populations.csv')
except IOError as e:
    print(e)
    exit()

pop_df = pop_list
dictionary = {'Country': pop_df['Country (or dependency)'].iloc[0:10]}
topten_popdf = pd.DataFrame(dictionary)
topten_popdf['Population'] = pop_df['Population (2020)'].iloc[0:10]
cov_df = pd.DataFrame()     # empty dataframe
for row in topten_popdf.itertuples():     # iterate incrementally down rows.
    cov_df = pd.concat([cov_df,
                        covid19_df[covid19_df['Country/Region'] == row[1]]])
    # concatenates successive rows into df

cov_df = cov_df.drop(columns=['Province/State', 'Lat', 'Long'])
cov_df['end'] = cov_df.iloc[:, -1]
cov_pop_df = pd.DataFrame()
cov_pop_df['Country'] = cov_df['Country/Region']
cov_pop_df['Population'] = cov_df['end']
cov_pop_df = cov_pop_df.groupby(['Country']).agg('sum')

merged = pd.merge(topten_popdf, cov_pop_df, on='Country',
                  suffixes=[' Total', ' Infected'])
merged['Normalized Percentage'] = (merged['Population Infected'] /
                                   merged['Population Total'])*100
merged = merged.drop(columns=['Population Total', 'Population Infected'])

fig = plt.figure()
plt.xlabel('Country')
plt.ylabel('Normalized % Pop. Infected')
plt.title('Normalized Infections of Top Ten Most Populous Countries')
plt.bar(merged['Country'], merged['Normalized Percentage'])
plt.show()
