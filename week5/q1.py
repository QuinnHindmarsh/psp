num = int(input('enter a possitve integer'))
count = 0

while num <= 0:
    num = int(input('enter a possitve integer'))

def odd(num,count):
    num1 = int(num * 3 + 1)
    print(count,'. ',num,' is odd so i will multiple it by 3 and add one. n = 3n+1 :',num1)
    return num1

def even(num,count):
    num1 = int(num / 2)
    print(count,'. ',num,' is even so i will divide it by 2. n = n/2 :',num1)
    return num1

while num != 1:
    if num % 2 == 0:
        num = even(num,count)
    else:
        num = odd(num,count)
    count += 1
print('The hailstone sequence took',count,'steps to reach 1')