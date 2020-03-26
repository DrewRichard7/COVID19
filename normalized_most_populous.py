
import pandas as pd
import matplotlib.pyplot as plt

path = '''COVID-19/csse_covid_19_data/csse_covid_19_time_series/\
time_series_covid19_confirmed_global.csv'''
url1 = 'https://www.worldometers.info/coronavirus/#countries'
try:
    # covid_19_list = pd.read_html(url2, attrs={'class': 'table'})
    # covid_19_list[0].to_csv('infected_countries_pop.csv')
    covid19_df = pd.read_csv('infected_countries_pop.csv')
except IOError as e:
    print(e)
    exit()

ur2 = 'https://www.worldometers.info/world-population/population-by-country/'
try:
    # pop_list = pd.read_html(url2, attrs={'class': 'table'})
    # pop_list[0].to_csv('populations.csv')
    pop_df = pd.read_csv('populations.csv')
except IOError as e:
    print(e)
    exit()

# DataFrame of top ten most populous countries
topten_popdf = pd.DataFrame(
    {'Country': pop_df['Country (or dependency)'].iloc[0:10]})
topten_popdf['Population'] = pop_df['Population (2020)'].iloc[0:10]

cov_df = pd.DataFrame()
for row in topten_popdf.itertuples():
    cov_df = pd.concat([cov_df,
                        covid19_df[covid19_df['Country,Other'] == row[1]]])
cols = ['NewCases', 'TotalDeaths', 'NewDeaths', 'TotalRecovered',
        'ActiveCases', r"Serious,Critical", 'Tot Cases/1M pop',
        'Tot Deaths/1M pop']
cov_df = cov_df.drop(columns=cols)
cov_df = cov_df.loc[:, ~cov_df.columns.str.contains('^Unnamed')]
cov_df.rename(columns={'TotalCases': 'Total Infections',
                       'Country,Other': 'Country'}, inplace=True)
cov_df = cov_df.reset_index(drop=True)
cov_df['Total Population'] = topten_popdf['Population']
cov_df['Percentage'] = (cov_df['Total Infections']
                        / cov_df['Total Population'])*100
print(cov_df)
fig = plt.figure()
plt.xlabel('Country')
plt.ylabel('Population Infected (%)')
plt.title('Normalized Infections of Top Ten Most Populous Countries')
plt.xticks(rotation=30)
plt.bar(cov_df['Country'], cov_df['Percentage'])
plt.show()
