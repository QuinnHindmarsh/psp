j = 1
k = 2

def func1():
    j = 3
    k = 4
    print('j = ',j, 'k = ',k)

def func2():
    j = 6
    func1()
    print('j = ', j, 'k = ', k)

k = 7
func1()
print('j = ', j, 'k = ', k)

j = 8
func2()
print('j = ', j, 'k = ', k)