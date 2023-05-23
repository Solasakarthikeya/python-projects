import random
import string

def generate_password(length):
    chars = string.ascii_letters + string.digits + string.punctuation
    print("the password is :")
    password = ''.join(random.choice(chars) for i in range(length))

    return password
password = generate_password(12)
print(password)
