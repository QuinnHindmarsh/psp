nums = [7, 8, 2, 0, 1, 6, 3, 4]
y = 0
x = 1

while x <= len(nums):
    y = y + nums[x-1]
    x = x + 1

print(y)
