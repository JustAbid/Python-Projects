import random
import string

pass_len = 8
CharVal = string.ascii_letters + string.digits + string.punctuation

password=""
for i in range(pass_len):
    password += random.choice(CharVal)

print("Your random password is: ", password)