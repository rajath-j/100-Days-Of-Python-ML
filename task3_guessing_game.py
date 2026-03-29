# task3_guessing_game.py

# 1. Set the secret number
secret_number = 7

print("Welcome to the Guessing Game!")
print("I'm thinking of a number between 1 and 10...")

# 2. Start the infinite loop
while True:
    # 3. Ask for the user's guess and convert it to an integer
    guess = input("Guess the secret number (between 1 and 10): ")
    guess = int(guess)

    # 4. Check if the guess is correct
    if guess == secret_number:
        print(" You win! You guessed it!")
        break  # This stops the infinite loop!

    elif guess > secret_number:
        print("Too high! Try again.")

    else:
        print("Too low! Try again.")