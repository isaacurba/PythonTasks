sum_of_integer = 0
product = 1
number = 0
largest = 0
for integers in range(1, 5):
    number = int(input(f"Enter integer number {integers}: "))    
    sum_of_integer = sum_of_integer + number 
    product = product * number
    if number > largest:
        largest = number
    
                                                                                                                                                                                                                                                                        
average = sum_of_integer / 4
print(f"The sum is {sum_of_integer}")
print(f"The average is {average}")
print(f"The product is {product}")
print(f"The largest is {largest}")
