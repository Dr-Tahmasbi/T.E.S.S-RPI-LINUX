#Guess The Number
import random
def play_guess_the_number(min_value, max_value):
  correct_number = random.randint(min_value, max_value)
  num_guesses = 0
  while True:
      num_guesses += 1
      user_guess = int(input("Enter the number I'm thinking of: "))
      if user_guess < correct_number:
        print("Your guess is too low.")
      elif user_guess > correct_number:
        print("Your guess is too high.")
      else:
        print(f"You've got it, I chose {correct_number}. It took you {num_guesses} guesses.")
        print(" ")
        break

def play_guess_the_number_main():
  min_num = int(input("What is the lowest number I can choose? "))
  max_num = int(input("What is the highest number I can choose? "))
  print("OK, let's play. How many guesses will you take?")
  play_guess_the_number(min_num, max_num)
#------------------------------------------------------------------------------------------------------------------
play_guess_the_number_main()
