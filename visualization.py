from matplotlib import pyplot as plt
import pandas as pd
import numpy as np

pd.set_option('display.width',320)

trainD = pd.read_csv('Data/train.csv')
testD = pd.read_csv('Data/test.csv')


tmp = trainD.drop(['id','comment_text'],axis=1)
x_labels = list(tmp.columns)
print(x_labels)
labels = np.arange(6)
width = 0.5

def sum_1(x):
    return (sum(x > 0))
def sum_0(x):
    return  (sum(x == 0))

y_0 = pd.Series.from_array(list(tmp.apply(sum_0,axis=0)))
y_1 = pd.Series.from_array(list(tmp.apply(sum_1,axis=0)))

fig = plt.figure()
ax = fig.add_subplot(111)
ax.set_xticks(labels+0.2)
ax.set_xticklabels(x_labels)

rects1 = ax.bar(labels,y_0,0.5)
rects2 = ax.bar(labels+width,y_1,0.5,color='r')

def chart(rects):
    for rect in rects:
        h = rect.get_height()
        ax.text(rect.get_x() + rect.get_width() / 2., 1.05 * h, '%d' % int(h),ha='center', va='bottom')

chart(rects1)
chart(rects2)
plt.show()