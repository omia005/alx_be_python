import random

def play_game():
  secret_number = random.randint(1, 10)
  guess = int(input("Please guess the number to be generated: "))

  match guess:
     case guess if secret_number == guess:
        print("Congratulations, You guessed correctly")
     case guess if secret_number < guess:
         print("Oops, your guess is a bit high. Try again!")
     case guess if guess < secret_number:
          print("Nope, your guess is a bit low. Give it another shot!")

while True:
    play_game()
    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again != "yes":
        print("Thanks for playing! Goodbye 👋")
        break