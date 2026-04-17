"""
1. prompt user to enter a password.
2. if:
-   password's length is less than 8 output is "Its very weak".
3. else if:
-   password's length is equal to 8, output is "Weak".
4 else if:
-   password's length is greater and equal to 8 and less than and equal to 16 output is "Strong"
5. else if:
-   password's length is greater and equal to sixteen output is "Very strong".
"""



password = input("Enter your password: ")
len_checker = len(password)
if len_checker < 8:
    print("very weak")
elif len_checker == 8:
    print("weak")
elif len_checker > 8 and password <= 16:
    print("strong")
elif len_checker > 16:
    print("very strong") 
    
