from itertools import permutations,combinations_with_replacement
import numpy as np
a = int(input())
d = 0
for i in permutations((range(1,a+1,1)), a):
    d += 1
print(d)
for i in permutations((range(1,a+1,1)), a):
    print(*i)

# g = 0
# for x in zip(a,b):
#     if x[0]!=x[1]:
#         g+=1







