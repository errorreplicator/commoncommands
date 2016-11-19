import matplotlib.pyplot as plt
import numpy as np

Y = [3, 4, 5, 3, 4]
X = [2, 3, 5, 7, 9]
x2 = [1,2,3,4,5]
y2 = [1,8,10,12,8]

# random 50 int numbers from 5 to 100
eage = np.random.random_integers(low=5,high=100,size=50)

#index of integers from 0 to len(eage) or this can be ranve(any_number_in_here) range(100)
ids = [x for x in range(len(eage))]

#buckets needed for histogram chart
#histogram of type chart
buckets = [0,10,20,30,40,50,60,70,80,90,100]
plt.hist(eage,buckets,histtype='bar')


# simple one array [y_true] value plot - plt takes one array and concider it as Y while generating X auto. starting from zero
plt.plot(Y)

# plotting X and Y values into LINE chart. X is always first
plt.plot (X,Y)

# two lines in chart
plt.plot(X,Y, label='1st line')
plt.plot(x2,y2, label = '2nd line')

#labels
plt.ylabel('Label Y')
plt.xlabel('Label X')

#Bar chart
plt.bar(X,Y,color='g')
plt.bar(x2,y2,color='c')

plt.title('Title of the chart\nSecond line')
plt.legend()
plt.show()