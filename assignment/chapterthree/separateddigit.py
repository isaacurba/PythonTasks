"""
UNDONE
separating digit logic
"""

number = int(input("Enter any digit number to separate the digit: "))
while number > 0:
#    print(number)
    number = number // 10
    print(number + " ")
    
