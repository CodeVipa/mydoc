from collections import ChainMap
dict1={'name':'Alice','age':20}
dict2={'name':'Joesph','age':30}
dict_chained=ChainMap(dict1,dict2)
print(dict_chained)
