global menue
menue = ['Margherita', 'Hawaiian', 'Pepperoni']

def display_details():
    print('author: Quinn Hindmarsh')
    print('email ID: hinqc001@mymail.unisa.edu.au')
    print("This is my own work as defined by the\nUniversity's Academic Misconduct Policy.\n\n")
display_details()

def print_menue():
    print("Pizza Menu:")
    print("============")
    print("1. Margherita")
    print("2. Hawaiian")
    print("3. Pepperoni")


def main():
    status = True
    current_order = []
    while status != False:
        order = input('do you want to order a pizza? (y/n): ')
        if order == 'y':
            current_order.append(get_pizza_choice())
        else:
            print('thanks for visiting!')
            status = False

    print('you have ordered the following pizzas:', current_order,'for a total of ',len(current_order),'pizzas')

def get_pizza_choice():
    print_menue()
    order = int(input('enter the number accosaited with the menue item you want to order: '))

    while order < 1 or order > 3:
        print('Invalid input')
        print_menue()
        order = int(input('enter the number accosaited with the menue item you want to order: '))

    print('you have ordered a', menue[order-1], 'pizza')

    return menue[order-1]

main()