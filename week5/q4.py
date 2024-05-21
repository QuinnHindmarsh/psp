status = False

def main():
    bottles = 100
    verses = int(input('how many verses would you like to sing? (1-100)'))
    while verses != 0 and verses > 100:
        verses = int(input('how many verses would you like to sing? (1-100)'))

    while (100 - bottles) < verses:
        print(bottles,'bottles of beer on the wall,',bottles,'bottles of beer')
        print('take one down, pass it around,',bottles-1,'bottles of beer on the wall')
        bottles -= 1


while status == False:
    sing = input('would you like to sing a song? (y/n): ').lower()
    if sing == 'y':
        status = True
        main()
    elif sing == 'n':
        status = True
        print('ok, maybe next time')
    else:
        print('invalid input')


