import pandas as pd
# import numpy as np
import sklearn.model_selection as sms
import sklearn.linear_model as sl
# import sklearn.svm as ss

ds = pd.read_csv('c:/ML/Data/breastc.data',names=['ID','label','x1','x2','x3','x4','x5','x6','x7','x8','x9'])
ds.drop('ID',1,inplace=True)

ds.drop(ds[ds.x5.str.contains(r'[?]')].index,0,inplace=True)
# print(ds.ix[ds.x5.str.contains(r'[?]')])
# print(ds.dtypes)
# print(ds.shape)
#
X = ds.drop('label',1)
y = ds['label']

X_train,X_test,y_train,y_test = sms.train_test_split(X,y,test_size=0.2)

clf = sl.LinearRegression()
clf.fit(X_train,y_train)
scr = clf.score(X_test,y_test)

print(scr)