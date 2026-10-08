import random

#Generates a random odd number between 1 and 1000
def generate_number():
    Number = random.randint(1,1000)
    
    while Number % 2 == 0:
      Number = random.randint(1,1000)
    return Number

# Checks if the guess is between 1 and 1000 and is an odd number
def is_valid_guess(guess):
  if 1 <= guess <= 1000 and guess % 2 == 1:
    return True
 
  else:
     return False 

# Returns a string indicating if the guess is too low, too high, or correct
def check_guess(guess, secret_number):
  if guess < secret_number:
    return "Too low"
  elif guess > secret_number:
    return "Too high" 
  else:
    return "Correct"
  
# Plays the game by checking the guess against the secret number
def play_game(secret_number, guess):
    return check_guess(guess, secret_number) 

# Gets the user's guess and converts it to an integer, returning None if the input is invalid
def get_guess(guess):
    try:
        return int(guess)
    except ValueError:
        return None

# Runs the game loop, prompting the user for guesses until they guess correctly
def run_game():
    secret_number = generate_number()

    while True:
        guess = input("Enter your guess: ")
        guess = get_guess(guess)

        if guess is None:
            print("Invalid input. Please enter a valid whole number.")
            continue

        if not is_valid_guess(guess):
            print("Invalid guess. Enter an odd number between 1 and 1000.")
            continue

        result = check_guess(guess, secret_number)
        print(result)

        if result == "Correct":
            break
if __name__ == "__main__":
    run_game()