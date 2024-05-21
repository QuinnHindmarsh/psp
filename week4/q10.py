import math
radii = [5, 2, 4, 3, 1]
y = 1

while y <= len(radii):
    print(radii[y-1] *(math.pi *math.pi))
    y = y + 1