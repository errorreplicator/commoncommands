import matplotlib.pyplot as plt
import numpy as np
import matplotlib

matplotlib.style.use('ggplot')

Y = [3, 4, 5, 3, 4]
X = [2, 3, 5, 7, 9]
x2 = [1,2,3,4,5]
y2 = [1,8,10,12,8]

# random 50 int numbers from 5 to 100
eage = np.random.random_integers(low=5,high=100,size=50)
eage2 = np.random.random_integers(low=5,high=50,size=50)

#index of integers from 0 to len(eage) or this can be ranve(any_number_in_here) range(100)
ids = [x for x in range(len(eage))]

# ----------------------------------------------plot set up ------------------------------------------------------------

# Plot size to 14" x 7"
matplotlib.rc('figure', figsize = (14, 7))
# Font size to 14
matplotlib.rc('font', size = 14)
# Do not display top and right frame lines
matplotlib.rc('axes.spines', top = False, right = False)
# Remove grid lines
matplotlib.rc('axes', grid = False)
# Set backgound color to white
matplotlib.rc('axes', facecolor = 'white')

# ----------------------------------------------------------------------------------------------------------------------


# simple one array [y_true] value plot - plt takes one array and concider it as Y while generating X auto. starting from zero
plt.plot(Y)

# plotting X and Y values into LINE chart. X is always first
plt.plot (X,Y)

# two lines in chart
plt.plot(X,Y, label='1st line')
plt.plot(x2,y2, label = '2nd line')

#Bar chart
plt.bar(X,Y,color='g')
plt.bar(x2,y2,color='c')
# --------------------------------------------Vertical bar chart -------------------------------------------------------
test_ds['Total'].plot(kind='barh',alpha=1,color='y')
test_ds['survived'].plot(kind='barh',alpha=0.5)
print(test_ds)
#---------------------------------------------histogram of type chart--------------------------------------------------#
buckets = [0,10,20,30,40,50,60,70,80,90,100] #buckets needed for histogram chart
plt.hist(eage) #simplest

plt.hist(eage,buckets,histtype='bar') #one data set

plt.hist(eage,buckets,histtype='bar',color = '#539caf',alpha=1) #two data sets
plt.hist(eage2,buckets,histtype='bar',color = '#7663b0',alpha=0.75)

# ----------------------------------------------------------------------------------------------------------------------
#-------------------------------------------#Scatter chart -------------------------------------------------------------

plt.scatter(eage,ids,color='b',marker='*',s=30)
plt.scatter(eage2,ids,color='r',marker='+',s=50)

# ----------------------------------------------------------------------------------------------------------------------


#Stack Plot
days = [1,2,3,4,5,6,7]
sleeping = [7,6,7,8,5,9,10]
eating = [2,3,1,1,2,2,3]
playing = [7,6,9,9,7,12,11]
working = [8,9,7,9,10,1,0]
plt.stackplot(days,sleeping,eating,playing,working,colors=['y','g','b','c'])

# Pie chart
slices = [4,5,1,11]
act = ['act1','act2','act3','act4']
plt.pie(slices,labels=act,colors=['c','m','w','y'])

#labels
plt.ylabel('Label Y')
plt.xlabel('Label X')


plt.title('Title of the chart\nSecond line')
plt.legend()
plt.show()