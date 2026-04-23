integer_sum = 0
while True:
    number = int(input("Enter any integer to print the sum: "))
    integer_sum += number
    if number == 0:
        break

print(integer_sum)
