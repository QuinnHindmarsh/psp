str1 = "These pretzels are making me thirsty!"
count = 0

for i in range(0, len(str1)):
    if str1[i] == 'e':
        count += 1

print('the number of "e"s is', count)

x = str1.isdigit()

if x == True:
    print('every letter is a digit')
else:
    print('not every letter is a digit')

print(str1.lower())
print(str1.upper())
print(str1.replace(' ','-'))