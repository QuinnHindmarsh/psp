def my_function(number):
    new_list = []
    index = 2
    while index < number:
        if number%index == 0:
            new_list.append(index)
        index += 1
    return new_list

print(my_function(24))