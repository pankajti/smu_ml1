import pandas as pd
import matplotlib.pyplot as plt

data_csv = '/Users/pankaj/dev/git/smu/smu_ml1/class3/moon/moon_landing.csv'
lnd_data= pd.read_csv(data_csv)
lnd_data = lnd_data[::2]
oper_outcom = pd.crosstab(lnd_data['Operator'], lnd_data['Outcome'],margins=True, margins_name="Total")
oper_outcom.sort_values('Total' , inplace=True)
oper_outcom= oper_outcom.drop('Total', axis=1)
ax = oper_outcom.plot(kind = 'barh', stacked = True, title='Moon Missions')
ax.set_xlabel('Number of Missions')
ax.set_ylabel('Operator')

plt.show()