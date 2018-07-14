import pandas as pd

stats = pd.read_csv('DemographicData.csv')

print(stats)

# method 2
import os

print(os.getcwd())
print(os.chdir('/usr/'))