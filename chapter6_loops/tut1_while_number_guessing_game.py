import random

# Generate a random secret number between 1 and 100
secret_number = random.randint(1, 100)

# Initialize variables
guess = None
attempts = 0

# Game loop
while guess != secret_number:
    guess = int(input("Guess the secret number (between 1 and 100): "))
    attempts += 1

    if guess < secret_number:
        print("Too low! Try again.")
    elif guess > secret_number:
        print("Too high! Try again.")
    else:
        print(
            f"Congratulations! You guessed the secret number {secret_number} in {attempts} attempts!"
        )
