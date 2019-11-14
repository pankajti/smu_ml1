import pandas as pd
from matplotlib import pyplot as plt

identity = pd.read_csv(r'/Users/pankaj/dev/git/smu/smu_ml1/kaggle/data/ieee/ieee-fraud-detection/train_identity.csv')

print(identity)

identity['id_01'].plot()
plt.show()

transactions = pd.read_csv(r'/Users/pankaj/dev/git/smu/smu_ml1/kaggle/data/ieee/ieee-fraud-detection/train_transaction.csv')

print(transactions)
from statsmodels.formula.api import ols