grade = int(input("Enter your grade: "))

if grade >= 90 and grade <= 100:
    print("A")
elif grade <= 89 and grade >= 80:
    print("B")
elif grade <= 79 and grade >= 70:
    print("c")
elif grade <= 69 and grade >= 60:
    print("D")
else:
    print("F")
