import random
die1 = random.randint(1, 6)
die2 = random.randint(1, 6)
x = 0
pair = 0
while x != 10:
    x = x + 1
    if die1 ==die2:
        print('You rolled a pair of',die1,'s')
        pair += 1
    else:
        print('you rolled a',die1,'and a',die2)

print('you rolled a pair',pair,'times out of 10 rolls.')
