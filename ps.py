password = input("Enter the password: ")


if len(password) >= 8:
        if password.isalnum():
            print("strong")
else:
    print("weak")