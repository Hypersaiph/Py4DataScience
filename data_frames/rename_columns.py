import pandas as pd

stats = pd.read_csv('DemographicData.csv')

print(stats.columns)
stats.columns = ['a', 'b', 'c', 'd', 'e']
print(stats.head())
stats.columns = ['CountryName', 'CountryCode', 'BirthRate', 'InternetUsers', 'IncomeGroup']
print(stats.head())
