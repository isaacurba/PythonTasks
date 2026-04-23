name = input("Enter a name to be reversed: ") 
reverse = "" 

for letter in reversed(name): 
    reverse += letter 

print(reverse)

