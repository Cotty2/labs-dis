from math import factorial
import math
import itertools

n = int(input())
k = int(input())

print('размещения')
print(math.factorial(n)/math.factorial(n - k))
s = []
for i in range(1, n + 1):
    s.append(i)
res = list(itertools.product(s, repeat=k))

print(res)

print('сочетания')
print(math.factorial(n)/(math.factorial(k) * math.factorial(n - k)))
print(math.comb(n, k))