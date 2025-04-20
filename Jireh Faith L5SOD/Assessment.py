from collections import ChainMap
import numpy as np
import matplotlib.pyplot as plt



store_A={
    'apple':1.2,
    'banana':0.5,
    'orange':0.8
}

store_B={
    'banana':0.4,
    'grape':2.0,
    'kiwi':1.5
}

store_C={
'orange':0.9,
'watermelon':3.0,
'apple':1.1
}
#combined dictionaries of stores
collections=ChainMap(store_A,store_B,store_C)
#printing the combined dic
print(collections)
#finding the price for banana in the combined stores
print(collections['banana'])
#updating the price of apple in store_A
store_A['apple']=1.3
#check if it has updated
print(f'the store_A has been updated: {store_A}')
print(collections['apple'])

 #question2
study_hours=[1,2,3,4,5,6,7,8,9,10]
scores=[52,57,61,63,65,68,72,76,78,85]
x=np.array(study_hours)
y=np.array(scores)


x_mean = sum(study_hours) / len(study_hours)
y_mean = sum(scores) / len(scores)
b1 = np.sum((x - x_mean) * (y - y_mean)) / np.sum((x - x_mean) ** 2)
b0 = y_mean - b1 * x_mean
# #for the intercept
c=y_mean-b1*x_mean
#predict the score
def predict_score(hours):
    return b1*hours+c
predicted_score=predict_score(12)
print(f'the predicted score for studying 12 hours is: {predicted_score}')
 #for the best fit line
plt.scatter(study_hours,scores,color='blue',label='actual scores')
plt.plot(study_hours,[predict_score(x) for x in study_hours],color='red',label='line of the best fit')
plt.xlabel('hours studied')
plt.ylabel('scores')
plt.title('study hours and the scores got')
plt.legend()
plt.show()

#Question3
height=5
for i in range(1,height+1):
    for j in range(i-1):
       print('*'*i)

