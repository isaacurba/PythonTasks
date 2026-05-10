"""
this code squares each digit of an array and print the sum of all the squared digit digit
"""
def mystery(x):
    y = 0
    for value in x:
        y += value ** 2
    return y

arr = [1, 2, 3]
print(mystery(arr))
