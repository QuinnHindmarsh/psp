import random

lotto = []
for x in range(1,9):
    lotto.append(random.randint(1,9))

for item in lotto:
    print(item,end=' ,')