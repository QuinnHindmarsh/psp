import random

def generate_password(length):
    password = ''
    for i in range(length):
        password += chr(random.randint(33,126))
    return password

print(generate_password(12))
