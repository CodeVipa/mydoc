import numpy as np
from scipy import stats

class_A=np.array([78,82,85,88,72,79,90,85,88,95])
class_B=np.array([68,72,77,80,74,78,82,84,76,80])
#mean for class A
mean_value=np.mean(class_A)
print(mean_value)
#mean for claaB
mean=np.mean(class_B)
print(mean_value)
#median for classA
median_value=np.median(class_A)
print(median_value)
#median for class B
median_value=np.median(class_B)
print(median_value)
#mode for classA
mode_value=stats.mode(class_A)
print(mode_value)
#mode for class B
mode_value=stats.mode(class_B)
print(mode_value)
#z-score for class A
z_score=stats.zscore(class_A)
print(z_score)
#z-score for class B
z_score=stats.zscore(class_B)
print(z_score)
#Based on the mean and z-scores,class B shows greater consistency in test scores