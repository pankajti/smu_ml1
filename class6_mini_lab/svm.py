import pandas as pd
from sklearn import  svm
from sklearn.linear_model import LogisticRegression
import matplotlib.pyplot as plt
from mlxtend.plotting import plot_decision_regions
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split


X = pd.DataFrame([[1,4], [1,2] , [2,6],[3,7] ,[3,1],[4,2], [6,3], [9,5], [8,2]])

y= pd.Series([1,1,1,1,0,0,0,0,0])

X_train , X_test, y_train, y_test = train_test_split( X, y, test_size   =0.1)
sc = StandardScaler()
sc.fit(X_train)
X_train_std = sc.transform(X_train)
X_test_std= sc.transform(X_test)
aa = sc.inverse_transform(X_train_std)
#plt.scatter(X[0], X[1], c= y)
svc = svm.SVC()
svc.fit(X, y)
print(svc.support_)
print(svc.support_vectors_)

log_reg = LogisticRegression()
log_reg.fit(X, y)
#plot_decision_regions(X.values, y.values, clf=svc, legend=2)
plot_decision_regions(X.values, y.values, clf=log_reg, legend=2)

plt.show()
