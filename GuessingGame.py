import random
def generate_number():
    Number = random.randint(1,1000)
    
    while Number % 2 == 0:
      Number = random.randint(1,1000)
    return Number
  
def is_valid_guess(guess):
  if 1 <= guess <= 1000 and guess % 2 == 1:
    return True
 
  else:
     return False 
   
def check_guess(guess, secret_number):
  if guess < secret_number:
    return "Too low"
  elif guess > secret_number:
    return "Too high" 
  else:
    return "Correct"
  
  
def play_game(secret_number, guess):
    return check_guess(guess, secret_number) 
  
def get_guess(guess):
    return int(guess)
  
def run_game():
    secret_number = generate_number()

    while True:
        guess = input("Enter your guess: ")
        guess = get_guess(guess)

        if not is_valid_guess(guess):
            print("Invalid guess. Enter an odd number between 1 and 1000.")
            continue

        result = check_guess(guess, secret_number)
        print(result)

        if result == "Correct":
            break
if __name__ == "__main__":
    run_game()