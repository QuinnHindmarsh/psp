
res = 3

def func():
    res = 4

func()
print(res)


res = 3

def func():
    global res
    res = 4

func()
print(res)