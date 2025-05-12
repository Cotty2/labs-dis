from math import factorial
import math
from itertools import *
import itertools

k=int(input())
n=int(input())

print('размещения')
print(n ** k)
s = [i for i in range(1, n + 1)]
s1 = [i for i in range(1, k + 1)]

res = list(itertools.product(s, repeat=k))
print(len(res))
print(res)


print('сочетания')
print(math.factorial(n + k - 1)/(math.factorial(k) * math.factorial(n - 1)))

res = list(itertools.combinations_with_replacement(s, k))
print(len(res))
print(res)