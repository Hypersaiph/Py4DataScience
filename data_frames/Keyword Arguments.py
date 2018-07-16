import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import warnings
warnings.filterwarnings('ignore')
plt.rcParams['figure.figsize'] = 8, 4

stats = pd.read_csv('DemographicData.csv')

stats.columns = ['CountryName', 'CountryCode', 'BirthRate', 'InternetUsers', 'IncomeGroup']

# changing the colors of the parameters
# increase size of the markers
vis1 = sns.lmplot(data=stats, x="InternetUsers", y="BirthRate", fit_reg=False, hue="IncomeGroup", size=8, scatter_kws={"s" : 200})
plt.show()