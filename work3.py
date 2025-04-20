import numpy as np
from scipy import stats 


customer_ratings=np.array([24, 18, 30, 15, 27, 19, 32, 22, 26, 17, 25, 31])
# mean value
mean_value=np.mean(customer_ratings)
print(mean_value)
#median value
median_value=np.median(customer_ratings)
print(median_value)
#mode value
mode_value=stats.mode(customer_ratings)
print(mode_value)
#z score
z_score=stats.zscore(customer_ratings)
print(z_score)
#there  are no outliers