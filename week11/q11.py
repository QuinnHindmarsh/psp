file = open('seinfeld.txt', 'r')
w = open('seinfeldOut3.txt', 'w')
line = file.readline()
while line:
    print(line, end="")
    w.write(line)
    line = file.readline()
