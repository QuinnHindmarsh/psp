#
# File: filename.py
# Author: your name
# Email Id: your email id
# Description: Practical 4.
# This is my own work as defined by the University's
# Academic Misconduct policy

"""
#will print 1-4
for k in range(4):
 print(k)
#nvm 0 - 3

#will print 0,2,4,6,8
for k in range(0,10,2):
 print('k is:', k)

"""
"""
#it will print each letter
string = 'Sooo much fun!'
for k in string:
    print(k)
"""
""""
#will print each letter again
string = 'Sooo much fun!'
for k in range(len(string)):
 print(string[k])
"""
'''
#will print every 2nd letter
string = 'Sooo much fun!'
for k in range(1,len(string),2):
 print(string[k])
'''
"""
#will print yes it is
fruit = ['apple', 'pear', 'banana', 'orange', 'watermelon']
if 'pear' in fruit:
 print('Yes it is!')
else:
 print('No it isn''t!')

#will print wtf!?!
str1 = 'Wednesday Thursday Friday'
new_string = ''
for char in str1:
 if char.isupper():
 new_string = new_string + char

new_string = new_string + '!?!'
print(new_string)

#will print all even nums
num_list = [3, 4, 8, 9, 2, 4, 7, 3, 1]
new_string = ''
index = 0
while index < len(num_list):
 if index % 2 == 0:
    new_string = new_string + str(num_list[index])

    index = index + 1
print(new_string)

#will print the sum of all even numbers
num_list = [3, 4, 8, 9, 2, 4, 7, 3, 1]
result = 0
index = 0
while index < len(num_list):
 if index % 2 == 0:
    result = result + num_list[index]

    index = index + 1
print(result)

#prints the sum of the numbers 0-9
result = 0
for index in range(10):
 result = result + index

print('Result is: ', result)
"""
#prints 6 # with a space and then !
for loop in range(3):
    for loop1 in range(1):
        for loop2 in range (2):
            print('#', sep='', end='')
            print(' ', sep='', end='')
print('!')

