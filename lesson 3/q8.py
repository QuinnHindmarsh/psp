import random

def base():
    even = 0
    odd = 0
    for i in range(0, 100):
        num = random.randint(1,1000)
        if num % 2 == 0:
            even = even + 1
        else:
            odd = odd + 1
    print('Even:', even, 'Odd:', odd)

def a():
    base()

a()

def b():
    for y in range(0, 10):
        a()
b()