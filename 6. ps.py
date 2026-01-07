password = input("Enter the password: ")
upper = False
lower = False
digit = False
special_character = False
special = "+^%$#@*!&"

if len(password) >= 8:
    for ch in password:
        if ch.isupper():
            upper = True
        if ch.islower():
            lower = True
    
        if ch.isdigit():
            digit = True
        if ch in special:
            special_character = True
else:
    print("Password must contain atleast 8 characters")


if upper & lower & digit & special_character:
    print("Strong")
elif upper & lower & digit:
    print("Medium")
else:
    print("Weak")
