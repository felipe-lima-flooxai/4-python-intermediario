from itertools import count

for i in count(10, 2):
    print(i)
    if i >= 20:
        break


c1 = count()

for x in c1:
    print(x)
    if x >= 40:
        break

