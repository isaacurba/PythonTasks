first_digit = int(input("Enter first digit: "))
second_digit = int(input("Enter second digit: "))
third_digit = int(input("Enter last digit: "))


total_sum = first_digit + second_digit + third_digit
average = total_sum / 3
product = first_digit * second_digit * third_digit


smallest = min(first_digit, second_digit, third_digit)
largest = max(first_digit, second_digit, third_digit)

print("Sum:\t",     total_sum)
print("Average:\t", average)
print("Product:\t", product)
print("Smallest:\t", smallest)
print("Largest:\t", largest)
