import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import warnings
warnings.filterwarnings('ignore')
plt.rcParams['figure.figsize'] = 8, 4

stats = pd.read_csv('DemographicData.csv')

stats.columns = ['CountryName', 'CountryCode', 'BirthRate', 'InternetUsers', 'IncomeGroup']

vis1 = sns.lmplot(data=stats, x="InternetUsers", y="BirthRate", fit_reg=False, hue="IncomeGroup")
plt.show()