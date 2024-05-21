name = str(input('enter a full name'))
x = name.split()

first_initial = x[0]
first_initial = first_initial[0]

middle_initial = x[1]
middle_initial = middle_initial[0]

last_initial = x[2]
last_initial = last_initial[0]

print(first_initial,middle_initial,last_initial, sep=' .',end='.')