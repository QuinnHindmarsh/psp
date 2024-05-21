import random

num = random.randint(1,10)
u_num = int(input('enter a number between 1 and 10'))

if u_num == num:
    print('you guessed the number')
else:
    print('better luck next time')
