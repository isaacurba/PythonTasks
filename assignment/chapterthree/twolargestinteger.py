largest = 0
second_largest = 0

for number in range(1, 11):
    integer = int(input(f"Enter integer {number}: "))
    
    if integer > largest:
        second_largest = largest
        largest = integer
    elif integer > second_largest:
        second_largest = integer

print(f"The largest is {largest}")
print(f"The second largest is {second_largest}")
