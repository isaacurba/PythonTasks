"""
1. user enters his purchased amount
2. the program does the logic on higher the price the the higher the discount:
- if
    purchased amount is greater and equal to 1,000 and the purchase amount is less than and equal to 10,000 discount should be 5%.
- else if
    purchased amount is greater than 10,000 and the purchase amount is less than and equal to 50,000 discount should be 10%.  
- else if
    purchased amount is greater and equal to 50,000 the discount is 20%.
3. The output should display the discount amount if it meets the conditions and subtract from original price.
"""

purchasedAmount = int(input("Enter your purchased amount to know your discount: "))
discountPrice = 0

if purchasedAmount >= 1000 and purchasedAmount <= 10000:
    discountPrice = purchasedAmount * (5 / 100)
elif purchasedAmount >= 10000 and purchasedAmount <= 50000:
    discountPrice = purchasedAmount * (10 / 100)
elif purchasedAmount >= 50000:
    discountPrice = purchasedAmount * (20 / 100)
else:
    print("You don't have a discount")
    
print(purchasedAmount - discountPrice)













