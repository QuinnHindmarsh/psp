initprice = int(input('what is the inital price? '))
discount = int(input('what is the percent discount? '))
discount = discount / 100

print('the new price is: ', initprice * (1-discount))