def func1():
    number1 = 0
    number2 = 7
    number3 = 2
    number1 = number2 + number3
    number3 = 9
    number1 = number3 - number2
    number2 = 7 * number1 + 6
    print(number1)
    print(number2)
    print(number3)

def func2():
    number1 = 2
    number2 = 7
    number3 = 3
    result = number1 * number2
    print(result)
    result = number3 * number2
    print(result)

def func3():
    number1 = 1
    number2 = 2
    number3 = 3
    number1 = number1 + 2
    number1 = number1 + number2
    number1 = number1 + number3
    print(number1)

def func4():
    number1 = 5
    number2 = 6
    number3 = 7
    result = 0
    number3 = number2 / 3
    number2 = number1 * number2
    number1 = number1 + 2
    print(number1, number2, number3)

def main():
    while True:
        num = int(input('Enter a number between 1 and 4: '))
        if num == 1:
            func1()
        elif num == 2:
            func2()
        elif num == 3:
            func3()
        elif num == 4:
            func4()


main()