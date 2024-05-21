import random

num = random.randint(1,100)
replay = 'y'

def main():
    status = False
    while status == False:
        guess = int(input('Enter a number: '))
        if guess == num:
            print('You win!')
            replay = input('Do you want to play again? (y/n): ')
            status = True
        elif guess > num:
            print('Too high')
        else:
            print('Too low')

if replay == 'y':
    main()
