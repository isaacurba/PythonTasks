"""
collect three three scores form users

calculate the average of the scores

grade the scores according to the average score
"""


total = 0
count = 3

for i in range(1, count + 1):
    score = int(input(f"Enter score {i}: "))
    total += score


average = total / count
print(f"Average: {average}")

if 90 <= average <= 100:
    print('Grade: A')
elif 80 <= average < 90:
    print('Grade: B')
elif 70 <= average < 80:
    print('Grade: C')
elif 60 <= average < 70:
    print('Grade: D')
elif 0 <= average < 60:
    print('Grade: F')
else:
    print("Invalid average")
