# Вход: a – упорядоченный по возрастанию список,
# x – число
# Выход: индекс наибольшего элемента i:
# a[i] <= x или -1, если такого индекса нет
def upper_bound(a, x):
    n = len(a)
    l = 0
    r = n - 1
    while l <= r:
        m = (l + r) // 2
        if a[m] <= x:
            l = m + 1
        else:
            r = m - 1
    return r


a = [1, 2, 3, 4, 5, 9999]
x = 9999
print(upper_bound(a, x))

a = [1, 2, 3, 4, 5, 9, 9, 10, 10000, 10000, 10001]
x = 4
print(upper_bound(a, x))

a = [0, 0, 1, 2, 3, 4, 5, 9, 9, 10, 10, 20, 20, 20, 20, 20]
x = 9
print(upper_bound(a, x))

a = [0, 99]
x = 99
print(upper_bound(a, x))

a = [1, 1, 1, 1, 1]
x = 9
print(upper_bound(a, x))

a = [0, 0, 0, 0, 0, 0, 0]
x = 9
print(upper_bound(a, x))

a = [-100000, -100, -100, 0]
x = -20
print(upper_bound(a, x))

a = []
x = 9
print(upper_bound(a, x))

a = [14, 14.5555, 14.55555]
x = 14.55554
print(upper_bound(a, x))

a = [0, 234, 3464, 45776, 4575688, 346457678]
x = 9099934939573
print(upper_bound(a, x))

a = [1, 1, 1]
x = 1
print(upper_bound(a, x))