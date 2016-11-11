import pandas as pd

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

# ??????????
print(ds['capital-gain'][ds['capital-gain'] == '?'])

#converts column fir to number
ds.fir = pd.to_numeric(ds.fir)
##ds['rc'] = ds['rc'].astype(np.float64)
##ds['wc'] = ds['wc'].astype(np.int64)