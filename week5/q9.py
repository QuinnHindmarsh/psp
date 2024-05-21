"""
a.

count = 1
while count <= 5:
    count = count + 1

print('Count is', count)
"""
"""
b.
mark = 69
grade = ''

if mark >= 85:
    grade = 'HD'
elif mark >= 75:
    grade = 'D'
elif mark >= 65:
    grade = 'C'
elif mark >= 55:
    grade = 'P1'
elif mark >= 50:
    grade = 'P2'
elif mark >= 40:
    grade = 'F1'
else:
    grade = 'F2'
print('The grade is:', grade)
"""


"""
c.
import random
play = 'y'

while play == 'y':

    # generate random number 1 - 100 inclusive
    number = random.randint(1,100)

    # prompt for and read user’s guess
    guess = int(input('Please enter your guess: '))
    print('')

    # determine whether user guessed correct random number
    while guess != number:
        if guess < number:
            print('Too low - please try again!')
            guess = int(input('Please enter your guess: '))
        else:
            print('Too high - please try again!')
            # prompt for and read user’s guess
            guess = int(input('Please enter your guess: '))
            print('')

    print('Well done - you guessed it!')

# prompt for and read whether the user would like to play again
    play = input('Would you like to play again (y/n)? ')
    print('')

"""