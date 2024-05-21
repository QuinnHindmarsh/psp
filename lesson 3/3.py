""""
#origonaly there would be a syntex error due to incorect indentation - once fixed it will print "WTF!?!"
str1 = 'Wednesday Thursday Friday'
new_string = ''
index = 0
while index < len(str1):
 if str1[index].isupper():
    new_string = new_string + str1[index]

 index = index + 1
new_string = new_string + '!?!'
print(new_string)
#it did
"""
""""
#PRINTS EVEN NUMS
str1 = '348924731'
new_string = ''
index = 0
while index < len(str1):
 if index % 2 == 0:
    new_string = new_string + str(str1[index])

 index = index + 1
print(new_string)
"""
"""
#prints even nums
str1 = '348924731'
new_string = ''
index = 0
while index < len(str1):
 if index % 2 == 0:
    new_string = new_string + str(str1[index])

 index = index + 1
print(new_string)
"""
"""
#should print 10, 55 if my maths is right
index = 0
result = 0
while index < 10:
 result = result + index

 index = index + 1
print('Result is: ', index, result)
#my maths is not right
"""
"""
#10, 0-9
index = 0
result = ''
while index < 10:
 result = result + str(index)

 index = index + 1
print('Result is: ', index, result)
"""

