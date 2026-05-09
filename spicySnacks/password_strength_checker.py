password = input("Enter your password to check the strength: ")
length = len(password)

if length <= 1:
    print("is invalid")
elif length < 6:
    print("Weak")
elif length <= 10:
    print("Medium")
else:
    print("Strong")
