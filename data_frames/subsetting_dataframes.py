# Three parts
# - Rows
# - Columns
# - Combine The Two

import pandas as pd

stats = pd.read_csv('DemographicData.csv')

# P1. Rows, starts at 0
#print(stats[21:26])

#print(stats[:10])

# show reverse
#print(stats[::-1])

# 20th row
#print(stats[::20])

# P2. Columns
# Only column
#print(stats['Country Name'])

# More column, use a list
#print(stats[['Country Name', 'Birth rate']].head())

# Quick access
stats.columns = ['CountryName', 'CountryCode', 'BirthRate', 'InternetUsers', 'IncomeGroup']
#print(stats.CountryCode)

# P3. Com ining the two
# subset 4:8, another subset's been applied
#print(stats[4:8][['Country Name', 'Birth rate']])
#print(stats[['Country Name', 'Birth rate']][4:8])
