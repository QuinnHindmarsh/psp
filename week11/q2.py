nums = []
for x in range(0, 20):
    nums.append(int(input('enter a number')))

x = 0
min = 0
max = 0
sum = 0
for item in nums:
    x +=1
    sum += item
    if item < min:
        min = item
    if item > max:
        max = item

print('The minimum number is: ', min)
print('The maximum number is: ', max)
print('The number of numbers entered is: ', x)
print('The sum of the numbers is: ', sum)
print('The average of the numbers is: ', sum/x)


