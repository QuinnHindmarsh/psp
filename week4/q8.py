string = 'fanta'
y = 0
x = 1
while x <= len(string):
    if string[x-1] == 'a':
        y = y + 1
    x = x +1

print(y)

print(string.count('a'))