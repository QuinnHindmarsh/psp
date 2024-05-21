#it prints an amount of hastags equal to the sum of the two numbers given. e.g. if you give the program the numbers 5 and 4 it will print 20 hastags

index1 = 0
index2 = 0
input1 = int(input("Enter an integer: "))
input2 = int(input("Enter another integer: "))
while index1 < input1:
    while index2 < input2:
        print("#",end="")
        index2 = index2 + 1
    print()
    index2 = 0
    index1 = index1 + 1

#nvm i didnt notice the print statment on line 11 that will create a new line after the each itteration of the nested loop, so it makes a table equal to the two numbers you give it
#first input is the amount of collums, 2nd is the amount of rows