import pandas as pd
import os
data_root = '/Users/pankaj/dev/data/nifty50'
import  matplotlib.pyplot as plt
import datetime as dt


df = pd.read_csv(os.path.join(data_root, 'nifty_fifty_companies.csv'))
df.groupby('Name').count()['Symbol'][0:10].plot(kind = 'bar')
plt.show()

df['Name'].plot(kind= 'bar')
print(df)



from sklearn.neighbors.nearest_centroid import NearestCentroid

# the parameters for the nearest centroid metric to test are:
#    l1, l2, and cosine (all are optimized)

clf = NearestCentroid(metric='euclidean')