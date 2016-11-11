import pandas as pd
import numpy as np
# output longer width of the colsole

desired_width = 320
pd.set_option('display.width', desired_width)

#random DataFrame
ds = pd.DataFrame(np.random.choice([0.9,4.1,'2ta',np.nan], size=(10,5)),columns=['fir','sec','thir','4th','5th'])
