"""
UNDONE
"""
largest = 0
while True:
    number = int(input("Enter multiple number to get the largest (Enter ""stop "" to terminate): "))
    if number > largest:
        largest = number
    elif number == "stop":
        break
