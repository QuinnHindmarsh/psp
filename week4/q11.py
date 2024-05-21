import random
num1 = random.randint(1,20)
for x in range(9):
    num2 = random.randint(1,20)
    if num2 > num1:
        num1 = num2
print(num1)