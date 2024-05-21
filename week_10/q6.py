def read_colour():
    done = False
    while done == False:
        done == True
        colour = str(input('enter a primary colour'))
        if colour != 'red' and colour != 'blue' and colour != 'yellow':
            print('not a valid colour or spelt wrong please enter either red green or blue')
            done == False


read_colour()