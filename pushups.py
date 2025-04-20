import matplotlib.pyplot as plt
import numpy as np

x=[10,15,20,25,30]
y=[25,30,45,50,65]


#finding xmean
xmean=np.mean(x)
print(xmean)
#finding ymean
ymean=np.mean(y)
print(ymean)

# finding slope
b1=np.sum((y-ymean)*(x-xmean))/np.sum((x-xmean)**2)
b0=ymean-b1*xmean

print(f'the slope is {b1}')
print(f'the intercept is {b0}')

def predict(advertising_budget):
    return b0+b1*predictable_value
predictable_value=35000
print(f'the expected sales revenue is: {predict(predictable_value)}')

#plot
plt.scatter(x, y, color='blue', label='Actual Data')
plt.plot(x, predictable_value, color='red', label='Regression Line')
plt.xlabel('Advertising Spend (in $1000s)')
plt.ylabel('Sales Revenue (in $1000s)')
plt.title('Advertising Spend vs Sales Revenue')
plt.legend()
plt.show()