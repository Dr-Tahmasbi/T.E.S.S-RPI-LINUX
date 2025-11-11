ASCII_ART = r'''
                            _.--.
                        _.-'_:-'||
                    _.-'_.-::::'||
               _.-:'_.-::::::'  ||
             .'`-.-:::::::'     ||
            /.'`;|:::::::'      ||_
           ||   ||::::::'     _.;._'-._
           ||   ||:::::'  _.-!oo @.!-._'-.
           \'.  ||:::::.-!()oo @!()@.-'_.|
            '.'-;|:.-'.&$@.& ()$%-'o.'\U||
              `>'-.!@%()@'@_%-'_.-o _.|'||
               ||-._'-.@.-'_.-' _.-o  |'||
               ||=[ '-._.-\U/.-'    o |'||
               || '-.]=|| |'|      o  |'||
               ||      || |'|        _| ';
               ||      || |'|    _.-'_.-'
               |'-._   || |'|_.-'_.-'
                '-._'-.|| |' `_.-'
                    '-.||_/.-'
'''
#Treasure Game
def gameanotherChoice():
  play = input("Would you like to play again? (yes/no): ")
  if play == "yes":
    treasuregamemain()
  elif play == "no":
    print(" ")
    break
def treasuregame():
  print(" ")
  print("Welcome to Treasure Island.")
  print(" ")
  print("Legend has it that there is some buried treasure on the island you are exploring… so you have decided to in search for it.")
  print(" ")
  choiceMade = input("Do you want to start the game? (yes/no): ").lower()
  print(" ")
  if choiceMade == "yes":
    treasuregamemain()
  elif choiceMade == "no":
    return
def treasuregamemain():
  print(" ")
  swim_or_wait = input("You come to a lake. Do you either want to wait for a boat, or swim across? (swim/wait): ")
  print(" ")
  if swim_or_wait == "swim":
    print("You get eaten by a hungry shark. Game over.")
    print(" ")
    gameanotherChoice()
  elif swim_or_wait == "wait":
    print("A boat arrives and you arrive at the island safely.")
    print(" ")
  cave_or_stay = input("You come to a cave, do you want to venture inside or walk on? (venture/walk): ")
  print(" ")
  if cave_or_stay == "venture":
    print("You are squished by boulders never to be seen again. Game over.")
    print(" ")
    gameanotherChoice()
  elif cave_or_stay == "walk":
    print("You walk away from the cave along a narrow track in the forest.")
    print(" ")
  crossroad_turn = input("You eventually reach a crossroads. Do you want to go left, right or straight? (left/right/straight): ")
  print(" ")
  if crossroad_turn == "left":
   print("You are trampled by a herd of wildebeest. Game over.")
   print(" ")
   gameanotherChoice()
  elif crossroad_turn == "straight":
    print("You get stung by a poisonous wasp. Game over.")
    print(" ")
    gameanotherChoice()
  elif crossroad_turn == "right":
    print("You march on and find the treasure, wahoo!")
    print(" ")
    print(ASCII_ART)
    print(" ")
    gameanotherChoice()
#------------------------------------------------------------------------------------------------------------------
treasuregame()