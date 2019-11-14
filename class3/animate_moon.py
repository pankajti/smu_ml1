import matplotlib.pyplot as plt
from matplotlib import animation
import numpy as np
from matplotlib import pyplot as plt
from matplotlib.animation import FuncAnimation
plt.style.use('seaborn-pastel')
import pandas as pd


data_csv = '/Users/pankaj/dev/git/smu/smu_ml1/class3/moon/moon_landing.csv'
lnd_data = pd.read_csv(data_csv)
lnd_data = lnd_data[::2]
launch_date = lnd_data['Launch date[1]']
lnd_data['launch_date'] = launch_date.str.split(' ').apply(lambda x: x[2][0:4])

fig=plt.figure()



def animate(i):
    year_land_data = lnd_data[lnd_data['launch_date'] <= str(1958+i)]
    oper_outcom = pd.crosstab(year_land_data['Operator'], year_land_data['Outcome'], margins=True,
                              margins_name="Total")
    oper_outcom.sort_values('Total', inplace=True)
    # plt.barh(oper_outcom.index, oper_outcom['Total'])

    oper_outcom = oper_outcom.drop('Total', axis=1)
    bar_moon = oper_outcom.plot( kind='barh', stacked=True, title='Moon Missions {}'.format(str(1958+i)))
    bar_moon.set_xlabel('Number of Missions')
    bar_moon.set_ylabel('Operator')

anim =animation.FuncAnimation(fig, animate,   repeat=False,blit=False,frames=400,
                             interval=100)
plt.show()

#anim.save('mymovie.mp4',writer=animation.FFMpegWriter(fps=10))
