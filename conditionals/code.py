import random

print("Welcome to the number guessing game!")
max = input("Type a number for top range: ")
max = int(max)
random_number = random.randint(0, max)
guesses = 0

while True:
    guess = input("Guess my secret number: ")
    guesses += 1

    if guess.isdigit():
        guess = int(guess)
    else:
        print("Enter a number: ")
        continue 
    if guess < random_number:
        print("Too low.")

    elif guess > random_number:
        print("Too high.")

    else:
        print(f"Nice. My secret number was {random_number}.")
        break
    
print(f"It took you {guesses} guesses.")
