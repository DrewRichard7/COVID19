
# VERY MESSED UP, NEEDS READDRESSING



import pandas as pd
import matplotlib.pyplot as plt

url1 = 'https://www.worldometers.info/world-population/population-by-country/'

# if it's been a while since this was run, uncomment the read_html & to_csv
# lines to import the latest data. Don't forget to comment the read_csv before
#  you do.
# make sure to recomment after import
try:
    # population_list = pd.read_html(url1, attrs={'class': 'table'})
    # population_list[0].to_csv('populations.csv')
    countries_population_df = pd.read_csv('populations.csv')
except IOError as e:
    print(e)
    exit()

url2 = 'https://www.worldometers.info/coronavirus/#countries'
try:
    # pop_list = pd.read_html(url2, attrs={'class': 'table'})
    # pop_list[0].to_csv('infected_countries_pop.csv')
    countries_infected_list = pd.read_csv('infected_countries_pop.csv')
except IOError as e:
    print(e)
    exit()
print(countries_infected_list.head())
infected_df = infected_list
dictionary = {'Country': infected_df['Country,Other'].iloc[0:10]}
topten_infected_df = pd.DataFrame(dictionary)
topten_infected_df['Infections'] = infected_df['TotalCases'].iloc[0:10]
infected_df = pd.DataFrame()
for row in topten_infected_df.itertuples():
    infected_df = pd.concat([infected_df,
                            population_df[population_df['Country\
 (or dependency)']
                             == row[1]]])
cols = ['Yearly Change', 'Net Change', 'Density (P/Km²)',
        'Land Area (Km²)', 'Migrants (net)', 'Fert. Rate',
        'Med. Age', 'Urban Pop %', 'World Share']
infected_df = infected_df.drop(columns=cols)
infected_df['end'] = infected_df.iloc[:, 3]
inf_pop_df = pd.DataFrame()
inf_pop_df['Country (or dependency)'] = infected_df['Country (or dependency)']
inf_pop_df['Population'] = infected_df['end']
inf_pop_df = inf_pop_df.groupby(['Country (or dependency)']).agg('sum')

merged = pd.merge(topten_infected_df, inf_pop_df, on='Country (or dependency)',
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
