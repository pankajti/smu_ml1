import numpy as np
from matplotlib import pyplot as plt
from matplotlib.animation import FuncAnimation
plt.style.use('seaborn-pastel')
import pandas as pd




data_csv = '/Users/pankaj/dev/git/smu/smu_ml1/class3/moon/moon_landing.csv'
lnd_data= pd.read_csv(data_csv)
lnd_data = lnd_data[::2]
launch_date = lnd_data['Launch date[1]']
lnd_data['launch_date'] = launch_date.str.split(' ').apply(lambda x : x[2][0:4])

year_land_data = lnd_data[lnd_data['launch_date'] <= '1958']
oper_outcom = pd.crosstab(year_land_data['Operator'], year_land_data['Outcome'],margins=True, margins_name="Total")
oper_outcom.sort_values('Total' , inplace=True)
#plt.barh(oper_outcom.index, oper_outcom['Total'])

oper_outcom= oper_outcom.drop('Total', axis=1)
#plt.barh(oper_outcom.index, oper_outcom['Total'])
bar_moon = oper_outcom.plot( kind = 'barh', stacked = True, title='Moon Missions {}'.format('1958'))

bar_moon.set_xlabel('Number of Missions')
bar_moon.set_ylabel('Operator')

for year in lnd_data['launch_date'].unique()[1:]:
    year_land_data = lnd_data[lnd_data['launch_date']<=year]
    oper_outcom = pd.crosstab(year_land_data['Operator'], year_land_data['Outcome'],margins=True, margins_name="Total")
    oper_outcom.sort_values('Total' , inplace=True)
    #plt.barh(oper_outcom.index, oper_outcom['Total'])

    oper_outcom= oper_outcom.drop('Total', axis=1)
    #plt.barh(oper_outcom.index, oper_outcom['Total'])
    bar_moon = oper_outcom.plot(ax = bar_moon, kind = 'barh', stacked = True, title='Moon Missions {}'.format(year))

    bar_moon.set_xlabel('Number of Missions')
    bar_moon.set_ylabel('Operator')

plt.show()