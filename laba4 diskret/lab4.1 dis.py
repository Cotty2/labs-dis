letters = ['А', 'В', 'Е', 'К', 'М', 'Н', 'О', 'Р', 'С', 'Т', 'У', 'Х']

count = 0

for l1 in letters:
    for d1 in range(10):
        for d2 in range(10):
            for d3 in range(10):
                if d1 == 0 and d2 == 0 and d3 == 0:
                    continue
                for l2 in letters:
                    for l3 in letters:
                        number = l1 + str(d1) + str(d2) + str(d3) + l2 + l3
                        print(number)
                        count = count + 1

print("Всего номеров:", count)
