import math

CC = []
CC.append(int(input('enter your credit card number (or a friends): ')))



cc = []
cc = list(map(int, str(CC[0])))

cc.reverse()
#print(cc)

x = 1

while x < len(cc):
    temp = 0
    temp = cc[x] * 2

    if temp > 9:
        TempList = []
        TempList.append(temp)
        TemperList = []
        TemperList = list(map(int, str(TempList[0])))

        cc[x] = (TemperList[0]+TemperList[1])

    else:
        cc[x] = cc[x] *2



    x += 2

#print(cc)
total = 0
for x in cc:
    total += x


#print(total)
if total % 10 == 0:
    print('card is valid')
else:
    print('card is not valid')