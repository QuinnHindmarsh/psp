status = True
sum = 0
while status == True:
    num = int(input('enter a number to sum or a neggative number to finish '))

    if num < 0:
        status = False
    else:
        sum += num


