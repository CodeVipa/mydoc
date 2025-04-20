
from scipy import stats
import numpy as np

x=[12,13,45,67,88,90,33]
y=[23,56,90,11,12,13,21]
X=np.array(x)
Y=np.array(y)

x_mean=np.mean(X)

y_mean=np.mean(Y)

#slope
b1=np.sum(((x-x_mean)*(y-y_mean))/np.sum((x-x_mean)**2))
#intercept
b0=y_mean-b1*x_mean
print(f'the intercept is: {b0}')
print(f'the slope is: {b1}')
#predicting the sales budget
def predict(advertising_budget):
    return b0+b1*advertising_budget
advertising_budget=6
predicted_sales=predict(advertising_budget)
print(f'the predicted sales of the house is: {predicted_sales}')