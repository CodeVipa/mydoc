from collections import ChainMap
from scipy import stats
import numpy as np


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
#finding the price for banana in the combined stores
print(collections['banana'])


