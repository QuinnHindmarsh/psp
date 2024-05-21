import random

num = random.randint(1,10)

#print('the random number is:', num)

num1 = int(input('guess a number from 1 to 10'))
#print('you guessed:',num1, 'the random number was:', num)
guess = False
while guess != True:
    if num1 == num:
        print('good jkob you guessed correctly ')
    elif num1 > num:
        print('to high')
    else:
        print('too low')