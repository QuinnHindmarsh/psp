#prints 6, 8, 12, 9, 72, 9
info = [2, 6, 3, 1, 5, 9, 12, 4]
print(info[1])
print(len(info))
print(info[-1])
print(info[info[4]])
print(info[1] * info[6])
index = 5
print(info[index])

info = [2, 'four', 6, 'eight', 10]
print(info[0])
print(info[1])
info[1] = 'two'
print(info[-1])
print(info[-2])
print(info[1])
print(info.count('four'))
print(info.index(6))

string1 = "These pretzels are making me thirsty!"
wordList = string1.split()
print(wordList)
for word in wordList:
    print(word)

names = ['Tony Stark', 'Lex Luthor', 'Selina Kyle', 'Bruce Wayne', 'Peter Parker']
for k in names:
    print(k)

names = ['Tony Stark', 'Lex Luthor', 'Selina Kyle', 'Bruce Wayne', 'Peter Parker']
print(names[1:4])