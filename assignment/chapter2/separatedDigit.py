user_input = input("Enter 5 digit number: ")
number = int(user_input)

if number < 10000 or number > 99999:
    print("Pls enter a 5 digit number")
else:
    first_digit = number // 10000
    second_digit = (number // 1000) % 10
    third_digit = (number // 100) % 10
    fourth_digit = (number // 10) % 10
    last_digit = number % 10

    print(f"{first_digit}   {second_digit}   {third_digit}   {fourth_digit}   {last_digit}")
