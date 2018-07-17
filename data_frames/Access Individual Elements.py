import pandas as pd

stats = pd.read_csv('DemographicData.csv')

stats.columns = ['CountryName', 'CountryCode', 'BirthRate', 'InternetUsers', 'IncomeGroup']

# .at ->even integer are treated as labels
# .iat -> for integer location
#print(stats.iat[3,4])

#print(stats.iat[0,1])

#print(stats.at[2, 'BirthRate'])


sub10 = stats[::10]
#print(sub10)

#print(sub10.iat[10,0]) # it counts from 0
print(sub10.at[10, 'CountryName']) # Looks for labels