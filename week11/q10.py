r = open('seinfeld.txt', 'r')
w = open('seinfeldOut2.txt', 'w')
txt = r.readlines()

for x in txt:
    print(x, end='')
    w.write(x)
