import random
global die1
global die2
die1 = 0
die2 = 0
status = False

def roll():
    die1 = random.randint(1,6)
    die2 = random.randint(1,6)

while status == False:
    roll()
    sum = die2 + die1
    point = 0
    print(sum)
    if sum == 7 or sum == 11:
        print('You win!')
        status = True
    elif sum == 2 or sum == 3 or sum == 12:
        print('You lose!')
        status = True
    else:
        point = sum
        while status == False:
            roll()
            sum = die2 + die1
            print(sum)
            if sum == 7:
                print('You lose!')
                status = True
            elif sum == point:
                print('You win!')
                status = True
            else:
                print('Roll again')
                status = False


