import pandas as pd

stats = pd.read_csv('DemographicData.csv')

# print(stats)

# method 2
import os

# print(os.getcwd())
# print(os.chdir('/usr/'))

# Exploring data
# 1. Full dataframe

#print(len(stats))
#print(stats.columns)

#print(len(stats.columns))

# 5. top rows
#print(stats.head()) # remember the brackets

# 6. bottom rows
#print(stats.tail(6))

# 7. information on the columns

#print(stats.info()) # as in R

#print(stats.describe())

print(stats.describe().transpose())

