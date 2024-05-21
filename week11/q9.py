
r = open('seinfeld.txt', 'r')
txt = r.read()
r.close()
print(txt)
w = open('seinfeldOut1.txt', 'w')
w.write(txt)
w.close()