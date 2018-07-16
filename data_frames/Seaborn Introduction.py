import inline as inline
import matplotlib
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import warnings
warnings.filterwarnings('ignore')
#%matplotlib inline
plt.rcParams['figure.figsize'] = 8, 4

stats = pd.read_csv('DemographicData.csv')

stats.columns = ['CountryName', 'CountryCode', 'BirthRate', 'InternetUsers', 'IncomeGroup']

#vis1 = sns.distplot(stats["InternetUsers"], bins=30)

# boxplots
vis2 = sns.boxplot(data=stats, x="IncomeGroup", y="BirthRate")
plt.show()
