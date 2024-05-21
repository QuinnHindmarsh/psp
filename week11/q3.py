number_list = []

for x in range(0,10):
    number_list.append(int(input('Enter a number: ')))

bottom = int(input('enter a bottom value'))
top = int(input('enter a top value'))

new_list = []
newer_list = []
spare_list = []
for x in range(len(number_list)):
    if x >= bottom and x <= top:
        new_list.append(number_list[x])
    elif x < bottom:
        newer_list.append(number_list[x])
    elif x > top:
        spare_list.append(number_list[x])


#write code that will print new_list in reverse without using slicing or list methods
for x in range(len(new_list)-1,-1,-1):
    newer_list.append(new_list[x])

for item in spare_list:
    newer_list.append(item)

print(newer_list)

