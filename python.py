from matplotlib import pyplot as plt
import statistics
from scipy import stats
import numpy as np

data=[1,2,3,4,5,6,7,8]
mean_value=stats.mean(data)
print(mean_value)
#mode value
mode_value=stats.mode(data)[0],[0]
print(mode_value)
#standard deviation

import numpy as np
import statistics
age=[18,19,18,20,47,40,10]
mean_value=statistics.mean(age)
print(mean_value)
#standard deviation
std_dev=np.std(age)
print(std_dev)
#z-score
for i in (0 , age):
  print(i)
     
z_score=(age-mean_value)/std_dev
print(z_score)
x=[61,56,81,90,43]
y=['kigali','gasabo','kinyinya','kagugu','batsinda']
plt.plot(x,y)
plt.title('areas lived in')
plt.xlabel(x)
plt.ylabel(y)
plt.show()
