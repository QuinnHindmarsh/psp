def print_menue():
    print("Pizza Menu:")
    print("============")
    print("1. Margherita")
    print("2. Hawaiian")
    print("3. Pepperoni")

def main():
    print_menue()
    order = int(input('enter the number accosaited with the menue item you want to order: '))

    while order < 1 or order > 3:
        print('Invalid input')
        print_menue()
        order = int(input('enter the number accosaited with the menue item you want to order: '))
    print('thanks for placing your order!')
main()