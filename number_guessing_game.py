import random

secret_number = random.randint(1, 50)
attempts = 0

print("Guess a number between 1 and 50")

while True:
    guess = int(input("Enter your guess: "))
    attempts += 1

    if guess > secret_number:
        print("Too high!")
    elif guess < secret_number:
        print("Too low!")
    else:
        print(f"🎉 Correct! You guessed it in {attempts} attempts.")
        break
