import pandas as pd
import numpy as np
# output longer width of the colsole

desired_width = 320
pd.set_option('display.width', desired_width)

#pickle
clf = sl.LinearRegression()
clf.fit(X_train,y_train)
pd.to_pickle(clf,'LRclf.pickle')
clf = pd.read_pickle('LRClf.pickle')

#random DataFrame
ds = pd.DataFrame(np.random.choice([0.9,4.1,'2ta',np.nan], size=(10,5)),columns=['fir','sec','thir','4th','5th'])

# Random floats
sampl = np.random.uniform(low=1,high=130,size=40)

# Random Ints
sampl = np.random.random_integers(low=1,high=130,size=30)

#index of integers from 0 to len(samp) or this can be range(any_number_in_here) range(100)
ids = [x for x in range(len(sampl))]
