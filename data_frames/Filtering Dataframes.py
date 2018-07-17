import pandas as pd

stats = pd.read_csv('DemographicData.csv')

stats.columns = ['CountryName', 'CountryCode', 'BirthRate', 'InternetUsers', 'IncomeGroup']

# Filtering is about rows
#print(stats.InternetUsers < 2)

filter = stats.InternetUsers < 2

#print(stats[filter])

filter2 = stats.BirthRate > 40

#print(stats[filter2])

# more conditions
filter3 = filter & filter2

#print(stats[filter3])

# and another one
#print(stats[stats.IncomeGroup == "High income"])

# unique categories
#print(stats.IncomeGroup.unique())

# Malta only
print(stats[stats.CountryName == "Bolivia"])