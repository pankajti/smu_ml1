import pandas as pd

df =  pd.read_csv('/Users/pankaj/dev/git/smu/smu_ml1/kaggle/data/titanic/train.csv')

print (df.head())

df.describe()