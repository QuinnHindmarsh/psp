xy = [4,3,2,1,0,'new','old']
print(xy)

for x in xy:
    print(x)

print(xy[0:3])
print(xy[-3:])
xy[4] = 'same'
print(xy)

print(xy[::-1])