import numpy as np
from scipy import stats
from matplotlib import pyplot as plt

x=[2,3,5,7,8]
y=[4,5,7,10,11]
month=[1,2,3,4,5]
#mean of x
mean_value_x=np.mean(x)
print(f'the mean for x values is: {mean_value_x}')
#mean of y
mean_value_y=np.mean(y)
print(f'the mean for y values is: {mean_value_y}')
#slope(b1)pip list

slope,intercept,r,p,st=stats.linregress(x,y)
def budget(x):
    return slope*x+intercept
print(st)
month=list(map(budget,x))
print(f'the slope is: {slope}')
print(f'the intercept is: {intercept}')
plt.scatter(x,y)
plt.plot(x,y)
plt.show()

