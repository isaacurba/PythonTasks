user_input = int(input("Enter value that's either 1 or 2: "))
wrongnumber = 0

while user_input > 2:
    print("Value is not 1 or 2")
    user_input = int(input("Enter value that's either 1 or 2: "))
    if user_input != 1 or user_input != 2:
        wrongnumber += 1
	
print(f"you made {wrongnumber} wrong guesses.")
