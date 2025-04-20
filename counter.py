from collections import Counter
crt1=Counter([1,3,2,2,3,2,3])
# crt1.update([2,3,3,,3,4])
common=crt1.most_common()
print(common)