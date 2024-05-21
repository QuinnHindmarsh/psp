nums = int(input('enter a series of single digit numbers'))



y = 0
x = 1
while x <= len(str(nums)):
    y += int(str(nums)[x-1])
    x += 1

print(y)
