import pandas as pd
import numpy as np

# generate random dataset
ds = pd.DataFrame(np.random.choice([0.9,4.1,'2ta',np.nan], size=(10,5)),columns=['fir','sec','thir','4th','5th'])

# renaming columns
ds.rename(columns={'col1':'First','col2':'2nd','col3':'3rd','Unnamed: 4':'4th'}, inplace=True)

# dropping column
ds.drop('Unnamed: 0',1,inplace=True)

#print row 1to 4  of columns starting from name '2nd' to end of column list
print(ds.loc[1:4,'2nd':])

# reads csv and providing names of the columns
ds = pd.read_csv('census.dat',names=['education', 'age', 'capital-gain', 'race', 'capital-loss', 'hours-per-week', 'sex', 'classification'])

#read csv ignoring spaces in columns
ds = pd.read_csv('census.dat', skipinitialspace=True)

#stripe out spaces in the x2 column
ds['x2'] = pd.core.strings.str_strip(ds['x2'])

# ??????????
# print(ds['capital-gain'][ds['capital-gain'] == '?'])
# print football[(football.wins > 10) and (football.team == "Packers")]


#prints out 5th column for only the rows where in fir = 0.9
print(ds['5th'][ds['fir']  == 0.9])
#converts column fir to number
ds.fir = pd.to_numeric(ds.fir)
##ds['rc'] = ds['rc'].astype(np.float64)
##ds['wc'] = ds['wc'].astype(np.int64)

# print types of columns
print(ds.dtypes)


# creating column base on values in different column
#simple example
ds['Gender'] = ds['Sex'].map({'male': 0, 'female':1}).astype(np.int)
#more advance example
def realF (a):
    if (a['Sex'] == 'female' or a['Pclass'] == 3 or a['Age'] < 18):
        return 1
    else:
        return 0

ds_titan['SurvivalRate'] = ds_titan.apply(realF,axis=1)

#group by
for i in range(1,4):
    print (i, len(ds_train[ (ds_train['Sex'] == 'male') & (ds_train['Pclass'] == i) ]))

# simple mean of one column
print(ds_train['Survived'].mean())
# advanced filtering
print(ds_train[(ds_train['Survived'] == 1) & ((ds_train['Sex'] != 'male') | (ds_train['Sex'] == 'male' ))])
print(ds_train.loc[ds_train['Age'].isnull(),['Name','Sex','Age']])

# Display only objects
print(ds.dtypes[ds.dtypes.map(lambda x: x=='object')])

