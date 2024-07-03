import random

# Function for you to guess the computer's number
def guess(x):
    # Generate a random integer between 1 and x
    random_number = random.randint(1, x)
    guess = 0
    # Loop until you guess the correct number
    while guess != random_number:
        guess = int(input(f'Guess a number between 1 and {x}: '))
        if guess < random_number:
            print('Sorry, guess again. Too low.')
        elif guess > random_number:
            print('Sorry, guess again. Too high.')
        
    print(f'Yay, congrats! You have guessed the number {random_number} correctly!!')

# Function for the computer to guess your number
def computer_guess(x):
    low = 1
    high = x
    feedback = ""
    while feedback != "c":
        if low != high:
            guess = random.randint(low, high)
        else: 
            guess = low  # could also be high because low = high

        feedback = input(f"Is {guess} too high (H), too low (L), or correct (C)?? ").lower()
        if feedback == 'h':
            high = guess - 1 
        elif feedback == 'l':
            low = guess + 1 

    print(f'Yay! The computer guessed your number, {guess}, correctly!!')

# Run the functions
print("Let's play a game where you guess the computer's number!")
guess(10)

print("\nNow, let's play a game where the computer guesses your number!")
computer_guess(10)
