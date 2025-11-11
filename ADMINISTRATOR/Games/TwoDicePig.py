import random
#Pig Game
def pig_roll():
  dice = [0, 0]
  dice[0] = random.randint(1, 6)
  dice[1] = random.randint(1, 6)
  return dice    

def pig_points(dice):
  if dice[0] == 1 and dice[1] == 1:
      return 0
  elif dice[0] == 1 or dice[1] == 1:
      return -1
  else:
      return dice[0] + dice[1]

def pig_game():
  random.seed()
  score = [0, 0, 0, 0]
  num_players = int(input("How many players? 1-4: "))
  player = 0
  new_player = True
  while score[player] <= 100:
      if new_player:
          print()
          print("------------------------------------")
          print("Player", player + 1, "it's your turn.")
          print("Your score is currently:", score[player])
          total = 0
          new_player = False
          turn_end = False
      print("Press Enter to roll the dice.")
      input()
      dice = pig_roll()
      result = pig_points(dice)
      print("You rolled a", dice[0], "and", dice[1])
      if result >= 0:
          print("You scored", result)
          total = total + result
          print("Your total is", total)
          choice = ""
          while choice not in ["y", "n", "q"]:
              choice = input("Do you want to continue y/n or (q)uit?:")
          if choice == "n":
              score[player] = score[player] + total
              turn_end = True
          elif choice == "q":
              break
      else:
          if result == -1:
              print("Oh no, that's a pig out!")
          else:
              print("Oh no, that's a double pig out, back to zero!")
              total = 0
          turn_end = True
      if turn_end:
          print("Press Enter to hand the dice to the next player.")
          input()
          player = (player + 1) % num_players
          new_player = True
#------------------------------------------------------------------------------------------------------------------
pig_game()
