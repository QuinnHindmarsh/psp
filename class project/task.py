def sum(a,b,c):
    return a + b + c

print(sum(1,2,3))

def find_item(list,value):
    try:
        return list.index(value)
    except:
        return -1

def find_item2(list,value):
    x = 0
    while x < len(list):
        if list[x] == value:
            return x
        x += 1
    return -1

list = ['p','q','r']
val = 'q'
print(find_item(list,val))

print(find_item2(list,val))
