day = int(input('enter a day'))
month = int(input('enter a month'))
year = int(input('enter a year (2 digits)'))

if day * month == year:
    print('{}/{}/{} is a magic number'.format(day,month,year))
else:
    print('{}/{}/{} is not a magic number'.format(day, month, year))