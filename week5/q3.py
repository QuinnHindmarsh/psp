accepted = ['red', 'blue', 'yellow']
def main():
    prim1 = input('enter a primary colour (red, blue, or yellow): ').lower()
    prim2 = input('enter a 2nd and different primary colour (red, blue, or yellow): ').lower()

    while prim1 not in accepted:
        print('invalid input')
        prim1 = input('enter a primary colour (red, blue, or yellow): ').lower()
    while prim2 not in accepted:
        print('invalid input')
        prim2 = input('enter a 2nd and different primary colour (red, blue, or yellow): ').lower()

    while prim1 == prim2:
        print('both colours cannot be the same, please reenter colour 2')
        prim2 = input('enter a 2nd and different primary colour (red, blue, or yellow): ').lower()

    combination(prim1,prim2)

def combination(prim1,prim2):
    if prim1 == 'red' and prim2 == 'blue':
        print('red and blue make purple')
    elif prim1 == 'red' and prim2 == 'yellow':
        print('red and yellow make orange')
    elif prim1 == 'blue' and prim2 == 'yellow':
        print('blue and yellow make green')



main()

