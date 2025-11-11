import os
import random
import time
import getpass

#colors and formats
BOLD = '\033[1m'
ITALIC = '\033[3m'
NORMAL = '\033[0m'
GRAY = '\033[30m'
RED = '\033[31m'
CYAN = '\033[36m'
GREEN = '\033[32m'
PURPLE = '\033[35m'
ORANGE = '\033[38;5;208m'
WHITE = '\033[37m'

emojis = {
  'armor': '\U0001F93A',
  'sword': '\U00002694',
  'shield': '\U0001F6E1',
  'chest': '\U0001F4E6',
  'health': '\U00002764',
  'crystal ball': '\U0001F52E',
  'bow': '\U0001F3F9',
  'dagger': '\U0001F5E1',
  'potion': '\U0001F9EA',
  'book': '\U0001F4D5'
}

#user name
user = getpass.getuser()

#player class
class Player():
  def __init__(self,hp,attk,magicka_attk,stamina,magicka,name):
    self.hp = hp
    self.attk = attk
    self.magicka_attk = magicka_attk
    self.stamina = stamina
    self.magicka = magicka
    self.name = name
    
  def attk_enemy(self,enemy):
    if self.stamina >= 5:
      print(f"{self.name} attacks {enemy.name}!")
      enemy.take_damage(self.attk)
      self.stamina -= 5
    else: print(f"{self.name} cannot attack with your current stamina!")
    
  def less_magicka(self,enemy):
    if self.magicka >= 5:
      print(f"{self.name} uses magicka on {enemy.name}")
      enemy.take_damage(self.magicka_attk)
      self.magicka -= 5
    else: print(f"{self.name} doesn't have enough magicka")
      
  def take_damage(self,damage):
    self.hp -= damage
    if self.hp <= 0:
      print(f"{self.name} has been defeated!")
      self.hp = 0
      game_over()

  def heal(self):
    if self.magicka >= 10:
      print(f"{self.name} heals!")
      self.hp += 5
      self.magicka -= 10
    else: print(f"{self.name} doesn't have enough magicka to heal!")

  def dodge_enemy(self):
    if self.stamina >= 5: return f"{self.name} dodged!"
    return f"{self.name} cannot dodge!"
        
#enemy class
class Enemy():
  def __init__(self,hp,attk,magicka_attk,stamina,magicka,name):
    self.hp = hp
    self.attk = attk
    self.magicka_attk = magicka_attk
    self.stamina = stamina
    self.magicka = magicka
    self.name = name

  def attk_player(self,player):
    if self.stamina >= 5:
      print(f"{self.name} attacked {player.name}!")
      player.take_damage(self.attk)
      self.stamina -= 5
    else: print(f"{self.name} cannot attack with your current stamina!")

  def less_magicka(self,player):
    if self.magicka >= 10:
      print(f"{self.name} used magicka on {player.name}!")
      player.take_damage(self.magicka_attk)
      self.magicka -= 10
    else: print(f"{self.name} doesn't has enough magicka...")
  
  def take_damage(self,damage):
    self.hp -= damage
    if self.hp <= 0:
      print(f"{self.name} has been defeated!")
      self.hp = 0

  def heal(self):
    if self.magicka >= 10:
      print(f"{self.name} heals!")
      self.hp += 5
      self.magicka -= 10
    else: print(f"{self.name} doesn't have enough magicka to heal!")

  def dodge_player(self):
    if self.stamina >= 5: return f"{self.name} dodged!"
    return f"{self.name} cannot dodge!"

#battle system
def battle(player,enemy):
  while player.hp > 0 and enemy.hp > 0:
    print(f"{GRAY}{player.name}{NORMAL} -- {RED}HP{NORMAL}: {player.hp} -- {GREEN}STAMINA{NORMAL}: {player.stamina} -- {CYAN}MAGICKA{NORMAL}: {player.magicka}")
    print(f"{enemy.name} -- {RED}HP{NORMAL}: {enemy.hp} -- {GREEN}STAMINA{NORMAL}: {enemy.stamina} -- {CYAN}MAGICKA{NORMAL}: {enemy.magicka}")
    time.sleep(3.5)
    os.system('clear')
    player_choice = str(input('[ATTACK] [MAGICKA] [HEAL] [DODGE] ')).strip()
    enemy_choice = random.choice(['attack','magicka','heal','dodge'])
    if player_choice.lower() == 'attack': player.attk_enemy(enemy)
    elif player_choice.lower() == 'magicka': player.less_magicka(enemy)
    elif player_choice.lower() == 'heal': player.heal()
    elif player_choice.lower() == 'dodge': player.dodge_enemy()
    if enemy_choice == 'attack': enemy.attk_player(player)
    elif enemy_choice == 'magicka': enemy.less_magicka(player)
    elif enemy_choice == 'heal': enemy.heal()
    elif enemy_choice == 'dodge': enemy.dodge_player()
    while player_choice.lower() not in ['attack','magicka','heal','dodge']:
      if player_choice.lower() == 'attack': player.attk_enemy(enemy)
      elif player_choice.lower() == 'magicka': player.less_magicka(enemy)
      elif player_choice.lower() == 'heal': player.heal()
      else: player.dodge_enemy()
      break

myCha = Player(0,0,0,0,0,'name')
comp = Enemy(0,0,0,0,0,'name')

#races
def races():
  global myCha
  print('Choose the class...')
  print(f"""{CYAN}{BOLD}Human{NORMAL} {GRAY}-> | High Strength | Low Magicka | High Stamina | High Health{NORMAL} \n{PURPLE}{BOLD}Mage{NORMAL} {GRAY}-> | Low Strength | High Magicka | High Stamina | Low Health{NORMAL} \n{GREEN}{BOLD}Orc{NORMAL} {GRAY}-> High Strength | Low Magicka | High Stamina | Low Health{NORMAL} \n{WHITE}{BOLD}Vampire{NORMAL} {GRAY}-> | Low Strength | High Magicka | Low Stamina | High Health{NORMAL}""")
  option = input('> ').strip()
  if option.lower() == 'human': myCha = Player(70,15,10,75,60,user)
  elif option.lower() == 'mage': myCha = Player(75,10,15,60,80,user)
  elif option.lower() == 'orc': myCha  = Player(70,15,20,80,55,user)
  elif option.lower() == 'vampire': myCha = Player(80,10,15,60,75,user)
  while option.lower() not in ['human','mage','orc','vampire']:
    if option.lower() == 'human': myCha = Player(70,20,10,75,60,user)
    elif option.lower() == 'mage': myCha = Player(75,10,15,60,80,user)
    elif option.lower() == 'orc': myCha  = Player(75,15,20,80,55,user)
    elif option.lower() == 'vampire': myCha = Player(80,10,15,60,75,user)
    break

#game over system
def game_over():
  print(f"{RED}Game Over{NORMAL}...")
  time.sleep(2.5)
  os.system('clear')
  main_menu()

#drop system
def drop():
  random_itens = random.choice(['armor','dagger','sword','bow','potion of magicka','potion of strength','potion of stamina','book of spells'])
  print(f"You got a {ORANGE}{random_itens}{NORMAL}")
  if random_itens == 'armor':
    myCha.hp += 20
    print(emojis['armor'])
  elif random_itens == 'dagger':
    myCha.attk += 5
    print(emojis['dagger'])
  elif random_itens == 'sword':
    myCha.attk += 15
    print(emojis['sword'])
  elif random_itens == 'bow':
    myCha.attk += 7
    print(emojis['bow'])
  elif random_itens == 'potion of magicka':
    myCha.magicka += 7
    print(emojis['potion'])
  elif random_itens == 'potion of strength':
    myCha.attk += 7
    print(emojis['potion'])
  elif random_itens == 'potion of stamina':
    myCha.stamina += 10
    print(emojis['potion'])
  else:
    myCha.magicka_attk += 15
    print(emojis['book'])

#computer enemies for easy battles
def comp_weak_character(char1,char2,char3,char4):
  global comp
  global myCha
  comp_choice = random.choice([char1,char2,char3,char4])
  if comp_choice == char1: comp = Enemy(45,5,10,65,60,char1)
  elif comp_choice == char2: comp = Enemy(45,10,15,65,60,char2)
  elif comp_choice == char3: comp = Enemy(50,10,15,65,60,char3)
  elif comp_choice == char4: comp = Enemy(55,10,15,65,70,char4)
  battle(myCha,comp) 

#computer enemies for medium or hard battles
def comp_character(char1,char2,char3,char4):
  global myCha
  global comp
  comp_choice = random.choice([char1,char2,char3,char4])
  if comp_choice == char1: comp = Enemy(50,10,15,70,60,char1)
  elif comp_choice == char2: comp = Enemy(55,10,15,75,60,char2)
  elif comp_choice == char3: comp = Enemy(60,10,22.5,75,60,char3)
  else: comp = Enemy(60,15,22.5,75,65,char4)
  battle(myCha,comp)

#hero camp
def hero():
  os.system('clear')
  print(f"{ITALIC}Hero campain...")
  print(f"In the {CYAN}Farren Village{NORMAL}, there's a terrible wave of monsters arriving to destroy everyone. You need to protect them. ")
  time.sleep(7)
  os.system('clear')
  print('prepare to fight...')
  time.sleep(2)
  os.system('clear')
  for c in range(1,5):
    print(f"wave {c}")
    comp_weak_character('Goblin','Zombie','Barbarian','Giant')
    drop()
    time.sleep(2)
    os.system('clear')
  print(f"{GREEN}Congrats{NORMAL}! Campain completed!!")
  input(f"press {GRAY}Enter{NORMAL} to continue: ")
  phases_menu()
  return True

#dragonstone camp
def dragonstone():
  os.system('clear')
  print(f"{CYAN}Dragonstone campain{NORMAL}...")
  print(f"{myCha.name}, a great traveler, was given to rescue the {BOLD}Dragonstone{NORMAL} from {GRAY}Castleland{NORMAL}")
  val = str(input(f'Do you want to know more about {WHITE}{BOLD}Dragonstone{NORMAL}? [Y/N]: ')).strip()[0]
  if val.lower() == 'y': 
    print(f"{BOLD}Dragonstone{NORMAL} is a rock table with powerful magic, which can be used to save the world or destroy it! ")
    time.sleep(7)
    os.system('clear')
    print("You finnaly arrived on Castleland...")
    time.sleep(3)
    os.system('clear')
    print('Look out, an enemy found you!')
    time.sleep(2)
    os.system('clear')
    comp_character('Skeleton','Knight Zombie','Dark Mage','Master Vampire')
    drop()
    time.sleep(3)
    os.system('clear')
    print(f"{myCha.name} found two ways to follow the path...")
    def path():
      global myCha
      global comp
      explore_right = False
      explore_left = False
      way = int(input('Right -- write 1\nLeft -- write 2\n> '))
      if way == 1:
        print("You are walking on a dark hall and found a fallen skeleton")
        drop()
        print("Look out! A creature has appeared!")
        comp_character('Skeleton','Knight Zombie','Dark Mage','Master Vampire')
        drop()
        explore_right = True
        input(f'Press {GRAY}Enter{NORMAL} to continue: ')
        path()
        while way == 1 and explore_right == True:
          print("You have already explored this way...")
          time.sleep(2)
          os.system('clear')
          path()
          break
      elif way == 2:
        print(f"You found the {WHITE}{BOLD}Dragonstone{NORMAL}!")
        time.sleep(2)
        os.system('clear')
        print(f"but, there's the {ORANGE}{BOLD}Morghor{NORMAL}, a Beholder, the Guardian of the {WHITE}{BOLD}Dragonstone{NORMAL}!")
        time.sleep(5)
        os.system('clear')
        print('prepare to fight...')
        time.sleep(2)
        os.system('clear')
        comp = Enemy(100,15,20,75,60,'Morghor')
        battle(myCha,comp)
        print(f"{ORANGE}{BOLD}Morghor{NORMAL} is defeted!! You rescued the {WHITE}{BOLD}Dragonstone{NORMAL}")
        print(f"{GREEN}Congrats{NORMAL}! Campain completed!")
        os.system('clear')
        phases_menu() 
        return explore_left == True
      while way not in [1,2]:
        os.system('clear')
        print("Invalid input...")
        time.sleep(2)
        os.system('clear')
        path()
        break
    path()
    
#tomb of the death camp
def tomb_of_the_death():
  global comp
  os.system('clear')
  print(f"{ORANGE}Tomb of the Death{NORMAL} campain...")
  print(f"the {CYAN}Farren Village{NORMAL} people was talking about a great mage, called Azher, that killed the village king and disappears...Some people said that the last time he has been seen, was in a great palace and also deadly place, wich is called Tomb of the Death.\n{myCha.name} is trying to find him and revenge the death of his king... ")
  time.sleep(10)
  os.system('clear')
  print('You entered in the Tomb of the Death and get faced with an enemy!')
  time.sleep(3)
  os.system('clear')
  comp_character('Thief','Mummy','Dark Wizard','Gargoyle')
  drop()
  time.sleep(3)
  os.system('clear')
  things = random.choice(['skull head on a throne','dead mage','dead warrior','destroyed tomb'])
  print(f"You found a {ORANGE}{things}{NORMAL}")
  if things == 'skull head on a throne' or things == 'destroyed tomb':
    drop()
    time.sleep(3)
    os.system('clear')
    drop()
    time.sleep(5)
    os.system('clear')
  else:
    drop()
    time.sleep(3)
    os.system('clear')
  print('A creature found you!!')
  time.sleep(3)
  os.system('clear')
  comp_character('Thief','Mummy','Dark Wizard','Gargoyle')
  drop()
  time.sleep(3)
  os.system('clear')
  print("Azher was found!\nHe summons a giant Skeleton to protect him...")
  time.sleep(3)
  os.system('clear')
  print('prepare to fight...')
  time.sleep(2)
  os.system('clear')
  for c in range(1,4):
    print(f'round {c}')
    comp = Enemy(90,10,15,75,80,'Master Skeleton')
    battle(myCha,comp)
    drop()
  print("Azher is defeated!")
  print(f"{GREEN}Congrats{NORMAL}! Campain completed!")
  time.sleep(5)
  os.system('clear')

#phase menu
def phases_menu():
  print(f'{WHITE}{BOLD}choose a campain phase...{NORMAL}')
  print()
  print("--------------------------")
  print(f"{GRAY}{BOLD}Hero{NORMAL}[1] -- {GREEN}easy\n{CYAN}{BOLD}Dragonstone{NORMAL}[2] -- {GRAY}medium\n{ORANGE}{BOLD}Tomb of the Death{NORMAL}[3] -- {RED}hard{NORMAL}\nBack[0]")
  print()
  choice = int(input('> '))
  if choice == 1: hero()
  elif choice == 2: dragonstone()
  elif choice == 3: tomb_of_the_death()
  elif choice == 0: 
    os.system('clear')
    main_menu()
  while choice not in [1,2,3,0]:
    print(f'{ITALIC}Invalid input...')
    choice = int(input('> '))
    if choice == 1: hero()
    elif choice == 2: dragonstone()
    elif choice == 3: tomb_of_the_death()
    elif choice == 0: 
      os.system('clear')
      main_menu()
    break
    
#main gameplay
def game():
  os.system('clear')
  print(f"{ITALIC}Prepare yourself...{NORMAL}")
  time.sleep(2.5)
  os.system('clear')
  races()
  time.sleep(1.5)
  os.system('clear')
  phases_menu()

#tutorial
def tut():
  os.system('clear')
  print("Training battle...")
  time.sleep(0.5)
  os.system('clear')
  races()
  os.system('clear')
  comp_character('Goblin','Troll','Dark Mage','Skeleton')
  input(f'press {BOLD}{GRAY}Enter{NORMAL} to back to menu: ')
  os.system('clear')
  main_menu()
  
#help
def help():
  os.system('clear')
  print(f"In this game it's good to know how the battle system works and which race is the best choice for you, [{GRAY}{user}{NORMAL}]")
  print()
  print(
    "Battle System: it contains four options to choose, attack - magicka - heal - dodge and the computer can also do these. As it was said before, you can choose your actions, but the computer will choose randomly. The battle system is based on stamina, so you need to have enough stamina to attack or dodge, and magicka enough to use magicka attack or healing."
    )
  print()
  print(
    "Races: there are four races -- human, mage, orc and vampire, each of them have different stats, so choose wisely. If you prefer melee fights, I suggest you to choose human or orc, else, you can choose mage or vampire, it depends on your preference."
  )
  print()
  print(
    "Stats: every time you take an action, it always appears your stats and the computer too, which contains health, stamina and magicka."
  )
  print()
  print("Drop: when you defeat an enemy, it will probally drops some itens, which can make you stronger to complete the campain, but it must to have luck, because the drop system has a random choice to drop certain items.")
  print()
  input(f"press {BOLD}{GRAY}Enter{NORMAL} to back to menu")
  os.system('clear')
  main_menu()

#main menu
def main_menu():
  print("################################")
  print("#    Dungeons : An RPG Game    #")
  print("#              Play            #")
  print("#            Tutorial          #")
  print("#              Help            #")
  print("#              Quit            #")
  print("################################")
  command = str(input('> ')).strip()
  if command.lower() in ['play','tutorial','help']:
    if command.lower() == 'play': game()
    elif command.lower() == 'tutorial': tut()
    elif command.lower() == 'help': help()
    elif command.lower() == 'quit': exit()
  while command not in ['play','tutorial','help','quit']:
    print(f'{ITALIC}Invalid command...')
    command = str(input('> ')).strip()
    if command.lower() == 'play': game()
    elif command.lower() == 'tutorial': tut()
    elif command.lower() == 'help': help()
    elif command.lower() == 'quit': break
    break
  
main_menu()