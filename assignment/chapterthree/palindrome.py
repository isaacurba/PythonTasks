original_number = int(input("Enter number to check if it's a palindrome: "))
number = original_number
reverse_digit = 0

while number > 0:
    last_digit = number % 10
    reverse_digit = (reverse_digit * 10) + last_digit
    number = number // 10  


if original_number == reverse_digit:
    print(f"{original_number} is a palindrome")
else:
    print(f"{original_number} is not a palindrome")

