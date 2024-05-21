import random

def generate_password(length):
    password = ''
    for i in range(length):
        password += chr(random.randint(33,126))
    return password

while True:
    length = int(input('Enter the length of the password: '))
    generate_password(length)
