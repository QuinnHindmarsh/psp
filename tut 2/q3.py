import random
#0 = heads, 1 = tails


status = False
while status != True:
    c1 = random.randint(0, 1)
    c2 = random.randint(0, 1)

    if c1 == 0 and c2 == 0:
        print('coin 1: heads')
        print('coin 2: heads')
        print('spinner wins')
        status = True
    elif c1 == 1 and c2 == 1:
        print('coin 1: tails')
        print('coin 2: tails')
        print('spinner loses')
        status = True
    else:
        if c1 == 1:
            print('coin 1: tails')
            print('coin 2: heads')
        else:
            print('coin 1: head')
            print('coin 2:tails')