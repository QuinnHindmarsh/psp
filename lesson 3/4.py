import random

die1 = random.randint(1,6)
die2 = random.randint(1,6)

if die2 == die1:
    print('you rolled a pair of', die1,'s')
else:
    print('you rolled a', die1, ' and a',die2)