grid = [
    'x','o','x'
    ,'o','x','o'
    ,'x','o','x'
]

for x in grid:
    print(x)

for x in range(0,9,3):
    print(grid[x],grid[x+1],grid[x+2],sep='|',end='\n')