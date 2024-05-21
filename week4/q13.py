#prints the string the user enters without the vouls it contains
#nvm the code is buggy and doesnt do anything
#it was just beacuse indentation was wrong
index = 0
output_string = ''
user_input = input("Enter a string: ")
while index < len(user_input):
    char = user_input[index]
    if char != 'a' and char != 'e' and char != 'i' and char != 'o' and char != 'u':
        output_string += char
    index += 1
print(output_string)