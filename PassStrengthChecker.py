import string

password = input("Enter your Password: ")

has_upper = False
has_lower = False
has_digit = False
has_special = False

special_Char = string.punctuation

for ch in password:
    if ch.isupper():
        has_upper = True
    elif ch.islower():
        has_lower = True
    elif ch.isdigit():
        has_digit = True
    elif ch in special_Char:
        has_special = True

if len(password) < 6:
    print("Weak password!")

elif( len(password) >= 10 and 
    has_upper and
    has_lower and
    has_digit and
    has_special
):
    print("Strong Password!")

else:
    print("Medium Password")