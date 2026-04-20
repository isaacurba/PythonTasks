print("Multiplication Table")
for number in range(1, 10):
#    print(f"{number} ")
#    print("__")
#    print(f"{number} |")
    for second_number in range(1, 10):
        print(f"{number * second_number:>2} ", end=" ")
    print()
        
