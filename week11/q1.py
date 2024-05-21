def determine_grade(mark):
    if mark >= 85:
        print('HD')
    if mark >= 75:
        print('D')
    if mark >= 65:
        print('C')
    if mark >= 55:
        print('P1')
    if mark >= 50:
        print('P2')
    if mark >= 40:
        print('f1')
    else:
        print('f2')


uinput= int(input('Enter your mark: '))
determine_grade(uinput)
