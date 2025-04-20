import numpy as np
from scipy import stats



dollars=np.array([24,18,30,15,27,19,32,22,26,17,25,31])
mean_value=np.mean(dollars)
print(mean_value)
#median
median_value=np.median(dollars)
print(median_value)
#mode
mode_value=stats.mode(dollars)
print(mode_value)
#z-score
z_score=stats.zscore(dollars)
print(z_score)
