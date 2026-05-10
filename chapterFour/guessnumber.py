import random

random_num = random.randint(1, 100)
guess = 0

print("Guess my number between 1 - 100")

while guess != random_num:

    guess = int(input("Guess: "))

    if guess > random_num:
        print("too high try again")
    elif guess < random_num:
        print("too low try again")
    else:
        print("congratulations, you guessed the number")
