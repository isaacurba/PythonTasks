principal = float(input("Enter amount you wish to borrow: "))

annual_interest = float(input("Enter the interest rate (e.g., 5.5): "))
monthly_interest = (annual_interest / 100) / 12

loan_duration = int(input("Enter duration in years: "))
number_of_payment = loan_duration * 12

numerator = monthly_interest * ((1 + monthly_interest) ** number_of_payment)
denominator = ((1 + monthly_interest) ** number_of_payment) - 1

mortgage = principal * (numerator / denominator)

print("Your monthly mortgage payment is: ", mortgage)
