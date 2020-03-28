# If it's been a while since this was run, uncomment the read_html & to_csv
# lines to import the latest data. Don't forget to comment the read_csv before
# you do.
# Make sure to recomment after import to avoid repetitive pinging of
# website's server.

import pandas as pd
import matplotlib.pyplot as plt

url1 = 'https://www.worldometers.info/world-population/population-by-country/'

# Import table of countries and their total population
try:
    # population_list = pd.read_html(url1, attrs={'class': 'table'})
    # population_list[0].to_csv('populations.csv')
    population_df = pd.read_csv('populations.csv')
except IOError as e:
    print(e)
    exit()

url2 = 'https://www.worldometers.info/coronavirus/#countries'
# Import table of countries and their population infected with COVID-19
try:
    # pop_list = pd.read_html(url2, attrs={'class': 'table'})
    # pop_list[0].to_csv('infected_countries_pop.csv')
    infected_df = pd.read_csv('infected_countries_pop.csv')
except IOError as e:
    print(e)
    exit()

# Create a dataframe of the top ten most infected countries
topten_infected_df = pd.DataFrame(
    {'Country': infected_df['Country,Other'].iloc[0:10]})
topten_infected_df['Infections'] = infected_df['TotalCases'].iloc[0:10]

# Here I had to change the nameprints in the csv files because one had UK
# and the other had United Kingdom, but for USA and S. Korea also.
# My skills aren't good enough yet to find and change that in code,
# so I did it manually.
# look at big_df = big_df.replace(to_replace=, value=)
big_df = pd.DataFrame()
for row in topten_infected_df.itertuples():
    big_df = pd.concat([big_df,
                        population_df[population_df['Country \
(or dependency)']
                                      == row[1]]])
cols = ['#', 'Yearly Change', 'Net Change', 'Density (P/Km²)',
        'Land Area (Km²)', 'Migrants (net)', 'Fert. Rate',
        'Med. Age', 'Urban Pop %', 'World Share']
big_df = big_df.drop(columns=cols)
big_df = big_df.loc[:, ~big_df.columns.str.contains('^Unnamed')]
big_df = big_df.reset_index(drop=True)
big_df.rename(columns={'Country (or dependency)': 'Country',
                       'Population (2020)': 'Total Population'}, inplace=True)
big_df['Infected Population'] = topten_infected_df['Infections']

# Here I added a column with the infections divided by population
# to normalize the data.
big_df['Percent Infected'] = (big_df['Infected Population'] /
                              big_df['Total Population'])*100

# Plot the data on a bar chart to show direct comparisons
fig = plt.figure()
plt.xlabel('Country')
plt.ylabel('Population Infected (%)')
plt.title('Normalized Infections of Top Ten Most Infected Countries')
plt.xticks(rotation=30)
plt.bar(big_df['Country'], big_df['Percent Infected'])
plt.show()
