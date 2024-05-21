number_set1 = [2, 3, 6, 7, 10, 11, 14, 15, 18, 19, 22, 23, 26, 27, 30, 31, 34, 35, 38, 39, 42, 43, 46, 47, 50, 51, 54, 55, 58, 59, 62, 63]
number_set2 = [8, 9, 10, 11, 12, 13, 14, 15, 24, 25, 26, 27, 28, 29, 30, 31, 40, 41, 42, 43, 44, 45, 46, 47, 56, 57, 58, 59, 60, 61, 62, 63]
number_set3 = [4, 5, 6, 7, 12, 13, 14, 15, 20, 21, 22, 23, 28, 29, 30, 31, 36, 37, 38, 39, 44, 45, 46, 47, 52, 53, 54, 55, 60, 61, 62, 63]
number_set4 = [16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63]
number_set5 = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51, 53, 55, 57, 59, 61, 63]
number_set6 = [32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63]

not_num = []

def add(UI,set):
    global not_num
    if UI == 'n':
        for item in set:
            try:
                not_num.index(item)
            except:
                not_num.append(item)

def find_not():
    global not_num

    for x in range(1,63):
        try:
            not_num.index(x)
        except:
            print('is ',x,'your number?')


print(number_set1)
UI = str(input('is your number in this grid y/n'))
add(UI,number_set1)

print(number_set2)
UI = str(input('is your number in this grid y/n'))
add(UI,number_set2)

print(number_set3)
UI = str(input('is your number in this grid y/n'))
add(UI,number_set3)

print(number_set4)
UI = str(input('is your number in this grid y/n'))
add(UI,number_set4)

print(number_set5)
UI = str(input('is your number in this grid y/n'))
add(UI,number_set5)

print(number_set6)
UI = str(input('is your number in this grid y/n'))
add(UI,number_set6)

print('\n\n')
not_num.sort()
find_not()
