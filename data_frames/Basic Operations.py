import pandas as pd

stats = pd.read_csv('DemographicData.csv')

# Operations:

stats.columns = ['CountryName', 'CountryCode', 'BirthRate', 'InternetUsers', 'IncomeGroup']

stats['MyCalc'] = stats.BirthRate * stats.InternetUsers

print(stats.head())

# Removing Column
stats = stats.drop('MyCalc', axis=1)
print(stats.head())