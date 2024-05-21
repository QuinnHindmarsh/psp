roman = {
    1:'I',
    2:'II',
    3:'III',
    4:'Iv',
    5:'V',
    6:'VI',
    7:'VII',
    8:'VII',
    9:'IX',
    10:'X'
}

num = int(input('enter a number between 1 and 10'))

if num <= 10:
    print(roman[num])
else:
    print('error number needs to be between 1 and 10')