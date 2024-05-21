"""
output:
homer simpson 
2 is a error as is - nvm my bad
mmmmmm Donuts
m
nuts
not sure about last one
"""
name1 = 'Homer'
name2 = 'Simpson'
name3 = 'Donuts'
print(name1 + ' ' + name2)
print(name1 + '\'s ' + name3)
print('m'*6 + ' ' + name3)
print(name1[2])
print(name3[2:6])
print(name1[0:4:1])
print(name2[-2])
print(len(name2))
fullName = name1 + ' ' + name2
if fullName == 'Homer Simpson':
 print('Doh!')
else:
 print('Bart - is that you?')