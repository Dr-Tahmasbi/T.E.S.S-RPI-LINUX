#T.E.S.S OS
#Created By Aidan Tahmasbi
#Property Of Tahmasbi Industries
#Based off MS-DOS
#RASPBERRY PI RELEASE ONLY
#-------------------------------------------------------------------------------------------------------------------
# Librarys
import webbrowser
import shutil
from pathlib import Path
from System.logo import LOGO
from System.logo import ERRORLOGO
from alive_progress import alive_bar
import colorama
from colorama import Fore, Back, Style
from contextlib import contextmanager
from io import StringIO
from cryptography.fernet import Fernet
import pandas as pd
import time
import random
import os
import sys
from os import system
import psutil
import speedtest
import socket
import requests
from io import StringIO
import pwinput
import getpass
from System.SlowTypeFunction import slowType
from faker import Faker
fake = Faker()
#-------------------------------------------------------------------------------------------------------------------
# Colors
BOLD = '\033[1m'
ITALIC = '\033[3m'
NORMAL = '\033[0m'
GRAY = '\033[30m'
RED = '\033[31m'
CYAN = '\033[36m'
GREEN = '\033[32m'
PURPLE = '\033[35m'
ORANGE = '\033[38;5;208m'
WHITE = '\033[37.0m'
ogdir = os.getcwd()
BLUE = colorama.Fore.BLUE
YELLOW = colorama.Fore.YELLOW
LIGHTGREEN = colorama.Fore.LIGHTGREEN_EX
lightYELLOW = Fore.LIGHTYELLOW_EX
black = colorama.Fore.LIGHTBLACK_EX
reset = colorama.Style.RESET_ALL
dim = Style.DIM
bold = Style.BRIGHT
#-------------------------------------------------------------------------------------------------------------------
# Important Variables
f = open(".secrets", "r")
keyStr = f.read()
url = 'https://newsapi.org/v2/top-headlines?sources=bbc-news&apiKey=ced0ce72796f4d9da3b0441d9ee0e85f'
userRunner = getpass.getuser()
response = requests.get(url)
listaaaa = response.json()
list2aaa = listaaaa['articles']
string_news = list2aaa[0]
dicti = string_news['title']
systemdirs = ["Documents", "Games", "Apps", "Messages", "Notes", "System", "TESS_OS.zip", "main.py", "tree.py", ".version", "Reminders.log", "ADMINISTRATOR"]
alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '_']
old = os.getcwd()
os.chdir(old)
closed=0
#------------------------------------------------------------------------------------------------------------------
# SUBPROGRAMS
#Dir System
def fullls():
  getdirectory()
  print("------")
  lista()
  folderscan()
  print("------")
def donotes():
  old = os.getcwd()
  os.chdir(home_directory + "Notes")

  print("------")
  try:
      if notes == 0:
          print("You don't have any notes. Let's make one!")
      else:
          if notes == 1:
              print("You currently have" + RED +
                    " 1 " + colorama.Style.RESET_ALL + "note.")
              print("------")
          else:
              print("You currently have " + RED +
                    str(notes) + colorama.Style.RESET_ALL + " notes.")
      print(
          "Would you like to do?...\n\n" + RED +
          "1)" + colorama.Style.RESET_ALL + " Create a note\n-- OR --\n" +
          RED + "2)" + colorama.Style.RESET_ALL +
          " Append (add) to a note?\n\nPlease use numbers (1 or 2) to answer."
      )
      valid = False
      while valid == False:
          choice = input(colorama.Style.RESET_ALL + termdes + " ")
          choice = str(choice)
          answers = ["1", "2"]
          if choice not in answers:
              print("Please use the" + RED +
                    " numbers 1 or 2 " + colorama.Style.RESET_ALL +
                    "to answer.")
              valid = False

          elif choice == "1" or choice == "2":
              valid = True
              break
      ###########################################################
      if choice == "1":
          print("------")
          print("What is the title of the note? ")
          valid = False
          while valid == False:
              title = input(colorama.Style.RESET_ALL + termdes + " ")
              if title.strip(" ") == "":
                  print("The name of the note cannot be blank!")
                  valid = False
              else:
                  valid = True
                  break

          filename = (f"{title}.txt")
          f = open(filename, "w")
          print("------")
          print(
              LIGHTGREEN +
              "Please write the note data below, and press Ctrl + C to save and exit."
              + colorama.Style.RESET_ALL)
          counter = 0
          while True:
              try:
                  counter = counter + 1
                  line = input(colorama.Style.RESET_ALL + RED + str(counter) +
                               ": " + colorama.Style.RESET_ALL)
                  f.write(line + "\n")
              except KeyboardInterrupt:
                  try:
                      print("---")
                      f.close()
                      print(colorama.Fore.LIGHTGREEN_EX +
                            "File successfully saved - '" +
                            RED + filename +
                            colorama.Fore.LIGHTGREEN_EX + "'" +
                            colorama.Style.RESET_ALL +
                            "\nFind your file in the folder 'Notes'")
                      print("------")
                      os.chdir(old)
                      break
                  except:
                      print()
                      print(colorama.Fore.RED + "File failed to save..." +
                            colorama.Style.RESET_ALL)
                      print("------")
                      os.chdir(old)
                      break
      if choice != "1":
          print("------")
          print("Which note would you like to add to?")
          dir = os.getcwd()
          dlist = dir.split("/")
          print("------")
          if str(dlist[-1]) != "":
              print("Directory: '" + RED +
                    str(dlist[-1]) + colorama.Style.RESET_ALL + "'")
          else:
              print("Directory: '" + RED +
                    "replit" + colorama.Style.RESET_ALL + "'")

          print("------")
          listfiles()
          if notes == 0:
              print(colorama.Fore.LIGHTBLACK_EX +
                    "This folder is empty,\nPress Ctrl+C to cancel..." +
                    colorama.Style.RESET_ALL)
          print("------")
          valid = False
          while valid == False:
              filename = input(colorama.Style.RESET_ALL + termdes + " ")
              try:
                  with open(filename) as f:
                      None
                  valid = True
              except:
                  print(colorama.Fore.RED + "\033[1mError: file: '" +
                        filename + "' not found.")
                  valid = False
          with open(filename) as f:
              contents = f.readlines()
          f.close()
          print("------")
          print("The contents of '" + RED +
                filename + colorama.Style.RESET_ALL + "':")
          print("------")
          for line in contents:
              print(line, end="")
              time.sleep(0.02)
          print()
          print("------")
          f = open(filename, "a")
          print(
              LIGHTGREEN +
              "Please write the note data below, and press Ctrl + C to save and exit."
              + colorama.Style.RESET_ALL)
          counter = 0
          while True:
              try:
                  counter = counter + 1
                  line = input(colorama.Style.RESET_ALL + RED + str(counter) +
                               ": " + colorama.Style.RESET_ALL)
                  f.write(line + "\n")
              except KeyboardInterrupt:
                  try:
                      print("---")
                      f.close()
                      print(colorama.Fore.LIGHTGREEN_EX +
                            "File successfully saved - '" +
                            RED + filename +
                            colorama.Fore.LIGHTGREEN_EX + "'" +
                            colorama.Style.RESET_ALL +
                            "\nFind your file in the folder 'Notes'")
                      print("------")
                      os.chdir(old)
                      break
                  except:
                      print()
                      print(colorama.Fore.RED + "File failed to save..." +
                            colorama.Style.RESET_ALL)
                      print("------")
                      os.chdir(old)
                      break

  except KeyboardInterrupt:
      print()
      print(colorama.Fore.RED + "Cancelling operation..." +
            colorama.Style.RESET_ALL)
      os.chdir(old)

def getdirectory():
  dir = os.getcwd()
  dlist = dir.split("/")
  print("------")
  if str(dlist[-1]) != "":
      print("Directory: '" + RED + str(dlist[-1]) +
            colorama.Style.RESET_ALL + "'")
  else:
      print("Directory: '" + RED + "replit" +
            colorama.Style.RESET_ALL + "'")


def ls():
  return os.listdir(os.getcwd())


def lista():
  files = os.listdir(os.getcwd())
  for location in files:
      sizea = int(os.path.getsize(str(os.getcwd()) + "/" + location))
      if sizea < 1000:
          size = str(
              os.path.getsize(str(os.getcwd()) + "/" + location)) + " B"
      if sizea < 1000000 and sizea > 1000:
          size = str(
              round(
                  os.path.getsize(str(os.getcwd()) + "/" + location) /
                  1000)) + " KB"
      if sizea >= 1000000 and sizea < 1000000000:
          size = str(
              round(
                  int(os.path.getsize(str(os.getcwd()) + "/" + location)) /
                  1000000)) + " MB"
      if sizea >= 1000000000 and sizea < 1000000000000:
          size = str(
              round(
                  int(os.path.getsize(str(os.getcwd()) + "/" + location)) /
                  1000000000)) + " GB"
      size = str(size)

      if location not in systemdirs:
          print(f"{'🗎' if os.path.isfile(location) else '🗀'}", end = "  ")    
          print("- '" + RED + location +colorama.Style.RESET_ALL + "'",end=" ")
      else:
          print(f"{'🗎' if os.path.isfile(location) else '🗀'}", end = "  ")    
          print("- '" + LIGHTGREEN + location +colorama.Style.RESET_ALL + "'",end=" ")
      print(f"({'file' if os.path.isfile(location) else 'folder'})" + " - " +
            colorama.Fore.LIGHTGREEN_EX + size + colorama.Style.RESET_ALL)

      time.sleep(0.02)


def listfiles():
  files = os.listdir(os.getcwd())
  for location in files:
      sizea = int(os.path.getsize(str(os.getcwd()) + "/" + location))
      if sizea < 1000:
          size = str(
              os.path.getsize(str(os.getcwd()) + "/" + location)) + " B"
      if sizea < 1000000 and sizea > 1000:
          size = str(
              round(
                  os.path.getsize(str(os.getcwd()) + "/" + location) /
                  1000)) + " KB"
      if sizea >= 1000000 and sizea < 1000000000:
          size = str(
              round(
                  int(os.path.getsize(str(os.getcwd()) + "/" + location)) /
                  1000000)) + " MB"
      if sizea >= 1000000000 and sizea < 1000000000000:
          size = str(
              round(
                  int(os.path.getsize(str(os.getcwd()) + "/" + location)) /
                  1000000000)) + " GB"
      size = str(size)

      if os.path.isfile(location):
          if location not in systemdirs:
              print(f"{'🗎' if os.path.isfile(location) else '🗀'}", end = "  ")    
              print("- '" + RED + location +colorama.Style.RESET_ALL + "'",end=" ")
          else:
              print(f"{'🗎' if os.path.isfile(location) else '🗀'}", end = "  ")    
              print("- '" + LIGHTGREEN + location +colorama.Style.RESET_ALL + "'",end=" ")
          print(f"({'file' if os.path.isfile(location) else 'folder'})" +
                " - " + colorama.Fore.LIGHTGREEN_EX + size +
                colorama.Style.RESET_ALL)

          time.sleep(0.02)

def listfilesExt(ext):
  filesO = os.listdir(os.getcwd())
  files = []
  for item in filesO:
      if item.endswith(ext):
          files.append(item)
      else:
          None
  if len(files) > 0:
      for location in files:
          sizea = int(os.path.getsize(str(os.getcwd()) + "/" + location))
          if sizea < 1000:
              size = str(
                  os.path.getsize(str(os.getcwd()) + "/" + location)) + " B"
          if sizea < 1000000 and sizea > 1000:
              size = str(
                  round(
                      os.path.getsize(str(os.getcwd()) + "/" + location) /
                      1000)) + " KB"
          if sizea >= 1000000 and sizea < 1000000000:
              size = str(
                  round(
                      int(os.path.getsize(str(os.getcwd()) + "/" + location)) /
                      1000000)) + " MB"
          if sizea >= 1000000000 and sizea < 1000000000000:
              size = str(
                  round(
                      int(os.path.getsize(str(os.getcwd()) + "/" + location)) /
                      1000000000)) + " GB"
          size = str(size)

          if os.path.isfile(location):
              if location not in systemdirs:
                  print(f"{'🗎' if os.path.isfile(location) else '🗀'}", end = "  ")    
                  print("- '" + RED + location +colorama.Style.RESET_ALL + "'",end=" ")
              else:
                  print(f"{'🗎' if os.path.isfile(location) else '🗀'}", end = "  ")    
                  print("- '" + LIGHTGREEN + location +colorama.Style.RESET_ALL + "'",end=" ")
              print(f"({'file' if os.path.isfile(location) else 'folder'})" +
                    " - " + colorama.Fore.LIGHTGREEN_EX + size +
                    colorama.Style.RESET_ALL)

              time.sleep(0.02)
  else:
      print(f"{black}No '{ext}' files found.{reset}")





def listfolders():
  files = os.listdir(os.getcwd())
  for location in files:
      sizea = int(os.path.getsize(str(os.getcwd()) + "/" + location))
      if sizea < 1000:
          size = str(
              os.path.getsize(str(os.getcwd()) + "/" + location)) + " B"
      if sizea < 1000000 and sizea > 1000:
          size = str(
              round(
                  os.path.getsize(str(os.getcwd()) + "/" + location) /
                  1000)) + " KB"
      if sizea >= 1000000 and sizea < 1000000000:
          size = str(
              round(
                  int(os.path.getsize(str(os.getcwd()) + "/" + location)) /
                  1000000)) + " MB"
      if sizea >= 1000000000 and sizea < 1000000000000:
          size = str(
              round(
                  int(os.path.getsize(str(os.getcwd()) + "/" + location)) /
                  1000000000)) + " GB"
      size = str(size)

      if not os.path.isfile(location):
          if location not in systemdirs:
              print(f"{'🗎' if os.path.isfile(location) else '🗀'}", end = "  ")    
              print("- '" + RED + location +colorama.Style.RESET_ALL + "'",end=" ")
          else:
              print(f"{'🗎' if os.path.isfile(location) else '🗀'}", end = "  ")    
              print("- '" + LIGHTGREEN + location +colorama.Style.RESET_ALL + "'",end=" ")
          print(f"({'file' if os.path.isfile(location) else 'folder'})" +
                " - " + colorama.Fore.LIGHTGREEN_EX + size +
                colorama.Style.RESET_ALL)

          time.sleep(0.02)

def checkfile():
  global valid, filename
  valid = False
  while valid == False:
      filename = input(colorama.Style.RESET_ALL + termdes + " ")
      try:
          with open(filename) as f:
              None
          valid = True
      except:
          print(colorama.Fore.RED + "\033[1mError: file: '" + filename +
                "' not found.")
          valid = False


def dirback():
  global parent
  parent = os.path.dirname(os.getcwd())
  os.chdir(parent)


def folderscan():
  DIR = os.getcwd()
  amount = len([
      name for name in os.listdir(DIR)
      if os.path.isfile(os.path.join(DIR, name))
  ])
  if amount == 0:
      print(colorama.Fore.LIGHTBLACK_EX + "This folder is empty." +
            colorama.Style.RESET_ALL)


def folderamount(folder):
  DIR = folder
  amount = len([
      name for name in os.listdir(DIR)
      if os.path.isfile(os.path.join(DIR, name))
  ])
  if amount == 0:
      print(colorama.Fore.LIGHTBLACK_EX + "This folder is empty." +
            colorama.Style.RESET_ALL)
  else:
      print("This folder contains " + RED +
            str(amount) + colorama.Style.RESET_ALL + " files")
#------------------------------------------------------------------------------------------------------------------
#System Information
def system_status():
  slowType(f"{black}This program is hardware dependent and has a chance of not working.{reset}", .02)
  print(" ")
  cpu_percent = psutil.cpu_percent(interval=1, percpu=True)
  cpu_freq = psutil.cpu_freq(percpu=True)

  print(f"{RED}CPU Usage Per Core:{reset}")
  for i, (percent, freq) in enumerate(zip(cpu_percent, cpu_freq), start=1):
    print(f"Core {i}: {percent}% Frequency: {freq.current} MHz")

  virtual_mem = psutil.virtual_memory()
  swap = psutil.swap_memory()
  print(f"{RED}\nVirtual Memory:{reset}")
  print(f"Total: {virtual_mem.total / (1024 ** 3):.2f} GB")
  print(f"Used: {virtual_mem.used / (1024 ** 3):.2f} GB")
  print(f"Swap Total: {swap.total / (1024 ** 3):.2f} GB")
  print(f"Swap Used: {swap.used / (1024 ** 3):.2f} GB")

  network = psutil.net_io_counters()
  print(f"{RED}\nNetwork Information:{reset}")
  print(f"Bytes Received: {network.bytes_recv}")
  print(f"Bytes Sent: {network.bytes_sent}")

  try:
    temperatures = psutil.sensors_temperatures()
    if temperatures:
      print("\nTemperature Information:")
      for name, entries in temperatures.items():
        for entry in entries:
          print(f"{name}: {entry.current} C")
    else:
      print(f"{RED}\nTemperature Information Unavailable.{reset}")
  except AttributeError:
    print(f"{RED}\nTemperature Information Unavailable.{reset}")

  #only if laptop
  battery = psutil.sensors_battery()
  if battery:
    plugged = "Plugged In" if battery.power_plugged else "Not Plugged In"
    print(f"{RED}\nBattery Status:{reset} {plugged}, {battery.percent}%")
  else:
    print(f"{RED}\nBattery Information Unavailable.{reset}")

  disk = psutil.disk_usage('/')
  print(f"{RED}\nDisk Information:{reset}")
  print(f"Total Disk Space: {disk.total / (1024 ** 3):.2f} GB")
  print(f"Used Disk Space: {disk.used / (1024 ** 3):.2f} GB")
  print(f"Free Disk Space: {disk.free / (1024 ** 3):.2f} GB")

  print(f"{RED}\nOS Information:{reset}")
  print("Tahmasbi Industries - Electromagnetic - Supercomputer - System")
  print("T.E.S.S OS vRPIos STABLE")
  print("DOS/UNIX Based OS")
  print("Raspberry Pi Release")
#------------------------------------------------------------------------------------------------------------------
#Internet Speed Test
def perform_speed_test():
    st = speedtest.Speedtest()
    servers = st.get_best_server()
    slowType("Testing download speed...", .02)
    download_speed = st.download() / 1000000  # Convert to Mbps
    slowType("Testing upload speed...", .02)
    upload_speed = st.upload() / 1000000  # Convert to Mbps
    return download_speed, upload_speed
#------------------------------------------------------------------------------------------------------------------
#clock
def clock():
  seconds = time.time()
  current_time = time.ctime(seconds)
  print(" ")
  print(current_time)
  print(" ")
  time.sleep(1)
#------------------------------------------------------------------------------------------------------------------
#Version
def version():
    print(" ")
    print("Tahmasbi Industries - Electromagnetic - Supercomputer - System")
    print("T.E.S.S OS vRPIos STABLE")
    print("DOS/UNIX Based Operating System")
    print("Raspberry Pi Release")
    print("Created and Licensed by Tahmasbi Industries")
    print(" ")
#------------------------------------------------------------------------------------------------------------------
#Help Function
def command_help(message_alert):
    print(f"{RED}You can press [CTRL][C] to exit any running program!{reset}")
    print(f"{RED}Press [CTRL][C] on the terminal to shut down T.E.S.S and return to the debian TTY.{reset}")
    print(" ")
    print("Commands:")
    print(" ")
    print(f"dir {black}Used to view files inside a directory.{reset}")
    print(f"cd {black}Used to enter a directory.{reset}")
    print(f"delete {black}Delete files.{reset}")
    print(f"whoami {black}Prints your username and access level{reset}")
    print(f"properties {black}Displays the properties of the chosen file(s){reset}")
    print(f"read {black}Read text files.{reset}")
    print(f"create {black}Create and view documents.{reset}")
    print(f"rename {black}Rename existing files{reset}")
    print(f"home {black}Reroutes back to home directory.{reset}")
    print(f"play {black}Play a selection of games.{reset}")
    print(f"apps {black}View and run all available applications.{reset}")
    print(f"version {black}Display the current version.{reset}")
    print(f"credits {black}Display the creators of T.E.S.S.{reset}")
    print(f"ipconfig {black}Displays current IP address.{reset}")
    print(f"help {black}Displays all available commands.{reset}")
    print(f"clear {black}Clears the console.{reset}")
    print(" ")
    print(" ")
    print("In-built System Applications:")
    print(" ")
    print("Notes")
    print(f"Messages {black}{message_alert}{reset}")
    print("EmployeeList")
    print("InternetSpeedTest")
    print("Clock")
    print("SystemInfo")
    print(" ")
#-------------------------------------------------------------------------------------------------------------------
#MAIN PROGRAM
#Loading Screen
pbarMessageNumber = random.randint(1, 8)
if pbarMessageNumber == 1:
    pbarMessage = "alive"
elif pbarMessageNumber == 2:
    pbarMessage = "wait"
elif pbarMessageNumber == 3:
    pbarMessage = "wait2"
elif pbarMessageNumber == 4:
    pbarMessage = "wait3"
elif pbarMessageNumber == 5:
    pbarMessage = "wait4"
elif pbarMessageNumber == 6:
    pbarMessage = "wait5"
elif pbarMessageNumber == 7:
    pbarMessage = "wait6"
elif pbarMessageNumber == 8:
    pbarMessage = "wait7"
print(LOGO)
with alive_bar(2000, title=f'{RED}LOADING T.E.S.S OS{reset}', length=30, spinner=pbarMessage, bar="blocks") as bar:
  for i in range(2000):
    time.sleep(.005)
    bar()
os.system("clear")
print(LOGO)
print(f"Welcome To {RED}T.E.S.S OS{reset} vRPIos STABLE.")
time.sleep(5)
os.system("clear")
#-------------------------------------------------------------------------------------------------------------------
#Username And Password
if userRunner != "root":
  if keyStr != "":
      keyBytes = bytes(keyStr, "utf-8")
      fernet = Fernet(keyBytes)
  else:
      print(f"{RED}The key value was empty. A new key has been generated. Previously accessible accounts may no longer be unlockable.{reset}")
      key = Fernet.generate_key()
      keyStr = str(key)[2:-1]
      keyBytes = bytes(keyStr, "utf-8")
      fernet = Fernet(keyBytes)
      time.sleep(2)
      f.close()
      f=open(".secrets", "w")
      f.write(keyStr)
      f.close()
      closed=1
  if closed == 0:
      f.close()
if userRunner != "root":
  #user code#
  valid = False
  validionormous = False
  while not validionormous:
      f = open("UWP.lock", "r")
      passdata = f.read().splitlines()
      f.close()
      try:
          while valid == False:
              slowType("T.E.S.S OS vRPIos STABLE", .02)
              username = input(f"Username: {black}Press [CTRL] and [C] to create new user...\n{reset}>>> ")
              if username.strip().lower() != "craw":
                  print("Searching usernames...")
              else:
                  if username not in os.listdir():
                      print(f"Use {black}Ctrl+C{reset} to create a new user {RED}Jonah{reset}.\n{CYAN}Stupid{reset} boy.")
                  else:
                      print(f"What {RED}Craw code{reset} are we writing today?")
              f=open("UWP.lock")
              contents = f.read()
              f.close()
              time.sleep(len(contents)/100)
              if username not in systemdirs and username in os.listdir():
                  for item in passdata:
                      if username in item.split(",")[0]:
                          correct = False
                          while correct == False:
                              if username in item:
                                  inlist = True
                                  passwordAttempt = pwinput.pwinput(prompt="Password:\n>>> ", mask="•")
                                  if passwordAttempt == fernet.decrypt(bytes(str(item.split(",")[1]), "utf-8")).decode():
                                      valid = True
                                      correct = True
                                      validionormous = True
                                      break
                                  else:
                                      correct = False
                                      print(f"{RED}Incorrect password{reset}\n------")
                      else:
                          None
                  correct = True
                  valid = True
                  validionormous = True
                  break
              else:
                  valid = False
                  print(f"{RED}Invalid username{reset}\n" + "------")
                  time.sleep(2)
                  os.system("clear")

      except KeyboardInterrupt:
          print("[CTRL]+[C]")
          time.sleep(1)
          os.system("clear")

          valid = False
          valid0 = True

          while valid == False and valid0 == True:
              valid1 = True
              done = 0
              username = input(f"New {CYAN}user{reset} username:\n>>> ")

              if username not in systemdirs and username in os.listdir():

                  valid = False
                  print(f"{RED}User already exists, please sign in.{reset}\n" + "------")
                  time.sleep(2)
                  os.system("clear")
                  valid0 = False
              for item in username:
                  if item.lower() in alpha:
                      None
                  else:
                      valid1 = False

              if valid1 ==False:
                  valid = False
                  print(f"{RED}Username must only contain letters and underscores.{reset}")
                  done = 1

              if len(username) >= 17.0:
                  valid = False
                  print(f"{RED}Username must be less than 17.0 characters.{reset}")
                  valid = False
                  done+=1

              print(f"Please enter a {RED}password{reset} for your new user. {black}(Type nothing for no password.){reset}")
              newPass = pwinput.pwinput(prompt=">>> ", mask="•")
              if newPass == "":
                  None
              else:
                  f=open("UWP.lock", "a")
                  newPass = fernet.encrypt(newPass.encode())
                  f.write(f"\n{username},{str(newPass)[2:-1]}\n")
                  f.close()

              ogdir = os.getcwd()
              if done >0:
                  time.sleep(2)
                  os.system("clear")



              else:   
                  valid = True
                  print(f"{PURPLE}Creating{reset} user...")
                  time.sleep(0.2)
                  shutil.copytree(ogdir + "/ADMINISTRATOR", username)
                  print(f"User {GREEN}created{reset}!")
                  time.sleep(1)
                  validionormous = True
                  break



  USER = username
  home_directory = os.getcwd() + "/" + username
  os.chdir(home_directory)
  time.sleep(1)
  os.system("clear")
if userRunner == "root":
    USER = "ADMINISTRATOR"
    username = "ADMINISTRATOR"
    home_directory = os.getcwd() + "/" + username
    os.chdir(home_directory)
    time.sleep(1)
    os.system("clear")
if username == "ADMINISTRATOR":
    UserAccessLevel = "Admin Account"
else:
    UserAccessLevel = "Regular Account"
    #end user code#
#-------------------------------------------------------------------------------------------------------------------
#Main Command-Line Interface
DIR = home_directory + "/Messages"
messages = len([
    name for name in os.listdir(DIR)
    if os.path.isfile(os.path.join(DIR, name))
])
DIR2 = home_directory + "/Notes"
notes = len([
    name for name in os.listdir(DIR2)
    if os.path.isfile(os.path.join(DIR2, name))
])
DIR = home_directory + "/Documents"
documents = len([
    name for name in os.listdir(DIR)
    if os.path.isfile(os.path.join(DIR, name))
])
if messages == 0:
    message_alert = ("No new messages.")
elif messages != 0:
    message_alert = (f"You have {messages} new message(s).")
try:
    os.chdir(home_directory)
    time.sleep(1)
    slowType("Welcome, " + RED + str(username) + reset + ".", .02)
    print("----------")
    slowType("BBC News: " + RED + str(dicti) + reset, .02)
    print("----------")
    slowType("Notifications: " + RED + str(message_alert) + reset, .02)
    print("----------")
    slowType("Version: " + RED + str("T.E.S.S OS, Version RPIos STABLE, Raspberry Pi Release, DOS/UNIX Based OS") + reset, .02)
    print("----------")
    print(" ")
    slowType("Type 'help' to get a list of commands.", .02)
    print(" ")
    while True:
        termdes = ("/> ")
        welcome = "\033[1m" + RED + username + RED + "@TESS - " + RED + reset + "/" + str(os.getcwd())
        prompt = welcome + termdes
        currentCommand = input(prompt).lower()
        if currentCommand == ("help"):
            command_help(message_alert)
            continue
        elif currentCommand == "ipconfig":
            try:
                hostname = socket.gethostname()
                ip_address = socket.gethostbyname(hostname)
                print("------")
                print(RED + "IP address: " +
                      colorama.Style.RESET_ALL + str(ip_address))
                print("------")
            except:
                print(colorama.Fore.RED + "An error occurred." +
                      colorama.Style.RESET_ALL)
        elif currentCommand == "rename":
            try:
                print("------")
                old = os.getcwd()
                print("Which" + RED + " file " +
                      colorama.Style.RESET_ALL + "would you like to\nRename?")
                getdirectory()
                print("------")
                lista()
                folderscan()
                print()
                valid = False
                while valid == False:
                    selection = input(colorama.Style.RESET_ALL + termdes + " ")
                    try:
                        with open(selection) as f:
                            None
                        f.close()
                        print()
                        valid = True
                    except:
                        try:
                            os.chdir(selection)
                            os.chdir(old)
                            valid = True
                        except:
                            print(colorama.Fore.RED + "\033[1mError: location '" +
                                  selection + "' not found.")
                            valid = False
                print("------")
                filename = selection
                try:
                    print("Location name: '" + colorama.Fore.LIGHTMAGENTA_EX +
                          selection + colorama.Style.RESET_ALL + "'")
                    print("What is the new name of the file?")
                    print("Please include the file extension" +
                          colorama.Fore.LIGHTMAGENTA_EX +
                          "\n(e.g: 'file.py', or 'music.mp3'" +
                          colorama.Style.RESET_ALL + ") in your response.\n")
                    selection = input(colorama.Style.RESET_ALL + termdes + " ")
                    try:
                        os.rename(filename, selection)
                        print(colorama.Fore.LIGHTGREEN_EX +
                              "File successfully renamed to: '" + selection + "'" +
                              colorama.Style.RESET_ALL)
                        print("------")
                    except:
                        print(colorama.Fore.RED +
                              "An error ocurred whilst renaming the file." +
                              colorama.Style.RESET_ALL)
                        print("------")
                except:
                    print(colorama.Fore.RED + "An error ocurred." +
                          colorama.Style.RESET_ALL)
                    print("------")
            except KeyboardInterrupt:
                print(colorama.Fore.RED + "Cancelling operation..." +
                      colorama.Style.RESET_ALL)
                print("------")
        elif currentCommand == "properties":
            try:
                old = os.getcwd()
                print("Which" + RED + " file " +
                      colorama.Style.RESET_ALL +
                      "would you like to\nGet the properties for?")
                getdirectory()
                print("------")
                lista()
                folderscan()
                print()
                valid = False
                while valid == False:
                    selection = input(colorama.Style.RESET_ALL + termdes + " ")
                    try:
                        with open(selection) as f:
                            None
                        f.close()
                        print()
                        valid = True
                    except:
                        try:
                            os.chdir(selection)
                            os.chdir(old)
                            valid = True
                        except:
                            print(colorama.Fore.RED + "\033[1mError: location '" +
                                  selection + "' not found.")
                            valid = False
                print("------")
                print("- File/folder '" + colorama.Fore.LIGHTMAGENTA_EX +
                      selection + colorama.Style.RESET_ALL + "'")

                if os.path.isfile(old + "/" + selection):
                    print("- Location type: " + colorama.Fore.LIGHTMAGENTA_EX +
                          "file" + colorama.Style.RESET_ALL)
                else:
                    print("- Location type: " + colorama.Fore.LIGHTMAGENTA_EX +
                          "folder" + colorama.Style.RESET_ALL)
                    folderamount(old + "/" + selection)

                size = os.path.getsize(old + "/" + selection)
                if size < 1000:
                    print("- Size: " + colorama.Fore.LIGHTMAGENTA_EX + str(size) +
                          " bytes")
                elif size >= 1000 and size < 1000000:
                    size = round(size / 1000)
                    print("- Size: " + colorama.Fore.LIGHTMAGENTA_EX + str(size) +
                          " kilobytes")
                elif size >= 1000000 and size < 1000000000:
                    size = round(size / 1000000)
                    print("- Size: " + colorama.Fore.LIGHTMAGENTA_EX + str(size) +
                          " megabytes")
                elif size >= 1000000000 and size < 1000000000000:
                    size = round(size / 1000000000)
                    print("- Size: " + colorama.Fore.LIGHTMAGENTA_EX + str(size) +
                          " gigabytes")

                print(colorama.Style.RESET_ALL + "- Location: " +
                      colorama.Fore.LIGHTMAGENTA_EX + os.getcwd() +
                      colorama.Style.RESET_ALL)
                os.chdir(old)

                print("------")
            except KeyboardInterrupt:
                print()
                print(colorama.Fore.RED + "Cancelling operation..." +
                      colorama.Style.RESET_ALL)
                print("------")
        elif currentCommand == "whoami":
            print("------")
            print(f"{RED}{username}{reset} {black}{UserAccessLevel}{reset}")
            print("------")
        elif currentCommand == ("clear"):
            os.system('clear')
            time.sleep(1)
            print("Welcome, " + RED + str(username) + reset + ".")
            print("----------")
            print("BBC News: " + RED + str(dicti) + reset)
            print("----------")
            print("Notifications: " + RED + str(message_alert) + reset)
            print("----------")
            print("Version: " + RED + str("TESS OS, Version RPIos STABLE, Raspberry Pi Release, DOS/UNIX Based OS") + reset)
            print("----------")
            print(" ")
            print("Type 'help' to get a list of commands.")
            print(" ")
            continue
        elif currentCommand == ("version"):
            version()
            continue
        elif currentCommand == ("home"):
            print(f"Navigating to {RED}User Directory{reset}.")
            print(" ")
            os.chdir(home_directory)
            continue
        elif currentCommand == "cd ..":
          dirback()
        elif currentCommand == "cd":
          try:
              print("------")
              print("Which folder would you like to enter?")
              print("------")
              listfolders()
              valid = False
    
              while valid == False:
                  selection = input(colorama.Style.RESET_ALL + termdes + " ")
                  try:
                      os.chdir(selection)
                      print(LIGHTGREEN +
                            "Successfully entered folder: '" +
                            RED + selection +
                            RED + "'" +
                            colorama.Style.RESET_ALL)
                      print("------")
                      valid = True
                  except:
                      print(colorama.Fore.RED + "\033[1mError: folder '" +
                            selection + "' not found.")
                      valid = False
          except KeyboardInterrupt:
              print()
              print(colorama.Fore.RED + "Cancelling operation..." +
                    colorama.Style.RESET_ALL)
              print("------")
        elif currentCommand == "read":
            try:
                print("------")
                print("Which file would you like to read?")
                dir = os.getcwd()
                dlist = dir.split("/")
                print("------")
                if str(dlist[-1]) != "":
                    print("Directory: '" + RED +
                          str(dlist[-1]) + colorama.Style.RESET_ALL + "'")
                else:
                    print("Directory: '" + RED +
                          "replit" + colorama.Style.RESET_ALL + "'")
                print("------")
                listfiles()
                DIR = os.getcwd()
                amount = len([
                    name for name in os.listdir(DIR)
                    if os.path.isfile(os.path.join(DIR, name))
                ])
                if amount == 0:
                    print(colorama.Fore.LIGHTBLACK_EX +
                          "This folder is empty,\nPress Ctrl+C to cancel..." +
                          colorama.Style.RESET_ALL)
                print("------")
                valid = False
                while valid == False:
                    filename = input(colorama.Style.RESET_ALL + termdes + " ")
                    try:
                        with open(filename) as f:
                            None
                        valid = True
                    except:
                        print(colorama.Fore.RED + "\033[1mError: file: '" +
                              filename + "' not found.")
                        valid = False
                with open(filename) as f:
                    contents = f.readlines()
                f.close()
                print("------")
                print("The contents of '" + RED +
                      filename + colorama.Style.RESET_ALL + "':")
                print("------")
                counter = 0
                index = -1
                print(contents)
                for line in contents:
                    index = index + 1
                    counter = int(counter)
                    counter = counter + 1
                    counter = str(counter)
                    line.replace(
                        "    ", colorama.Fore.LIGHTBLACK_EX + "•" +
                        colorama.Style.RESET_ALL)
                    print(counter + ":", line, end="")
    
                    time.sleep(0.02)
                print()
                print("------")
            except KeyboardInterrupt:
                print()
                print(colorama.Fore.RED + "Cancelling operation..." +
                      colorama.Style.RESET_ALL)
        elif currentCommand == "create":
            old = os.getcwd()
            os.chdir(home_directory + "/Documents")
    
            print("------")
            try:
                if documents == 0:
                    print("You don't have any documents. Let's make one!")
                else:
                    if documents == 1:
                        print("You currently have" +
                              RED + " 1 " +
                              colorama.Style.RESET_ALL + "document.")
                        print("------")
                    else:
                        print("You currently have " +
                              RED + str(documents) +
                              colorama.Style.RESET_ALL + " documents.")
                print(
                    "Would you like to do?...\n\n" +
                    RED + "1)" +
                    colorama.Style.RESET_ALL + " Create a file\n-- OR --\n" +
                    RED + "2)" +
                    colorama.Style.RESET_ALL +
                    " Append (add) to a file?\n\nPlease use numbers (1 or 2) to answer."
                )
                valid = False
                while valid == False:
                    choice = input(colorama.Style.RESET_ALL + termdes + " ")
                    choice = str(choice)
                    answers = ["1", "2"]
                    if choice not in answers:
                        print("Please use the" + RED +
                              " numbers 1 or 2 " + colorama.Style.RESET_ALL +
                              "to answer.")
                        valid = False
    
                    elif choice == "1" or choice == "2":
                        valid = True
                        break
                ###########################################################
                if choice == "1":
                    print("------")
                    print("What is the title of the file (with file extension)? ")
                    valid = False
                    while valid == False:
                        title = input(colorama.Style.RESET_ALL + termdes + " ")
                        if title.strip(" ") == "":
                            print("The name of the file cannot be blank!")
                            valid = False
                        else:
                            valid = True
                            break
    
                    filename = title
                    f = open(filename, "w")
                    print("------")
                    print(
                        LIGHTGREEN +
                        "Please write the file data below, and press Ctrl + C to save and exit."
                        + colorama.Style.RESET_ALL)
                    counter = 0
                    while True:
                        try:
                            counter = counter + 1
                            line = input(colorama.Style.RESET_ALL + colorama.Fore.LIGHTMAGENTA_EX +
                                         str(counter) + ": " +
                                         colorama.Style.RESET_ALL)
                            f.write(line + "\n")
                        except KeyboardInterrupt:
                            try:
                                print("---")
                                f.close()
                                print(colorama.Fore.LIGHTGREEN_EX +
                                      "File successfully saved - '" +
                                      RED + filename +
                                      colorama.Fore.LIGHTGREEN_EX + "'" +
                                      colorama.Style.RESET_ALL +
                                      "\nFind your file in the folder 'Documents'")
                                print("------")
                                os.chdir(old)
                                break
                            except:
                                print()
                                print(colorama.Fore.RED +
                                      "File failed to save..." +
                                      colorama.Style.RESET_ALL)
                                print("------")
                                os.chdir(old)
                                break
                if choice != "1":
                    print("------")
                    print("Which file would you like to add to?")
                    dir = os.getcwd()
                    dlist = dir.split("/")
                    print("------")
                    if str(dlist[-1]) != "":
                        print("Directory: '" + RED +
                              str(dlist[-1]) + colorama.Style.RESET_ALL + "'")
                    else:
                        print("Directory: '" + RED +
                              "replit" + colorama.Style.RESET_ALL + "'")
                    print("------")
                    listfiles()
                    if documents == 0:
                        print(colorama.Fore.LIGHTBLACK_EX +
                              "This folder is empty,\nPress Ctrl+C to cancel..." +
                              colorama.Style.RESET_ALL)
                    print("------")
                    valid = False
                    while valid == False:
                        filename = input(colorama.Style.RESET_ALL + termdes + " ")
                        try:
                            with open(filename) as f:
                                None
                            valid = True
                        except:
                            print(colorama.Fore.RED + "\033[1mError: file: '" +
                                  filename + "' not found.")
                            valid = False
    
                    with open(filename) as f:
                        contents = f.readlines()
                    f.close()
                    print("------")
                    print("The contents of '" + RED +
                          filename + colorama.Style.RESET_ALL + "':")
                    print("------")
                    for line in contents:
                        print(line, end="")
                        time.sleep(0.02)
                        print()
                    print("------")
                    f = open(filename, "a")
                    print(
                        LIGHTGREEN +
                        "Please write the file data below, and press Ctrl + C to save and exit."
                        + colorama.Style.RESET_ALL)
                    counter = 0
                    while True:
                        try:
                            counter = counter + 1
                            line = input(colorama.Style.RESET_ALL + RED +
                                         str(counter) + ": " +
                                         colorama.Style.RESET_ALL)
                            f.write(line + "\n")
                        except KeyboardInterrupt:
                            try:
                                print("---")
                                f.close()
                                print(colorama.Fore.LIGHTGREEN_EX +
                                      "File successfully saved - '" +
                                      RED + filename +
                                      colorama.Fore.LIGHTGREEN_EX + "'" +
                                      colorama.Style.RESET_ALL +
                                      "\nFind your file in the folder 'Documents'")
                                print("------")
                                os.chdir(old)
                                break
                            except:
                                print()
                                print(colorama.Fore.RED +
                                      "File failed to save..." +
                                      colorama.Style.RESET_ALL)
                                print("------")
                                os.chdir(old)
                                break
    
            except KeyboardInterrupt:
                print()
                print(colorama.Fore.RED + "Cancelling operation..." +
                      colorama.Style.RESET_ALL)
                os.chdir(old)
        elif currentCommand == "messages":
          if messages != 0:
              print("------")
          try:
              if messages == 0:
                  print("You currently have no messages.")
                  print("------")
              else:
                  if messages == 1:
                      print("You currently have" +
                            RED + " 1 " +
                            colorama.Style.RESET_ALL + "message.")
                      print("------")
                  else:
                      print("You currently have " +
                            RED + str(messages) +
                            colorama.Style.RESET_ALL + " messages.")
    
                  old = os.getcwd()
                  os.chdir(home_directory + "/Messages")
    
                  print("Which file would you like to read?")
                  print("------")
                  listfiles()
                  if messages == 0:
                      print(colorama.Fore.LIGHTBLACK_EX +
                            "This folder is empty,\nPress Ctrl + C to cancel..." +
                            colorama.Style.RESET_ALL)
                  print()
                  valid = False
                  while valid == False:
                      selection = input(colorama.Style.RESET_ALL + termdes + " ")
                      try:
                          with open(selection) as f:
                              contents = f.readlines()
                          f.close()
                          print()
                          print(LIGHTGREEN +
                                "Successfully obtained file contents." +
                                colorama.Style.RESET_ALL)
                          print()
                          print(RED +
                                "Message contents:\n" + colorama.Style.RESET_ALL)
                          print("----------------")
                          for line in contents:
                              print(line, end="")
                              time.sleep(0.02)
                          print()
                          print("----------------")
                          print()
                          valid = True
                          os.chdir(old)
                      except:
                          print(colorama.Fore.RED + "\033[1mError: file: '" +
                                selection + "' not found.")
                          valid = False
    
          except KeyboardInterrupt:
              print()
              print(colorama.Fore.RED + "Cancelling operation..." +
                    colorama.Style.RESET_ALL)
              print("------")
        elif currentCommand == "delete":
          old = os.getcwd()
          try:
              print("------")
              print("Which " + RED + "file " +
                    colorama.Style.RESET_ALL + "would you like to delete?")
              print(
                  colorama.Fore.RED +
                  "Be careful when deleting files that you don't own.\nMake sure you know what you're doing!"
                  + colorama.Style.RESET_ALL)
              getdirectory()
              print("------")
              listfiles()
              DIR = os.getcwd()
              amount = len([
                  name for name in os.listdir(DIR)
                  if os.path.isfile(os.path.join(DIR, name))
              ])
              if amount == 0:
                  print(colorama.Fore.LIGHTBLACK_EX +
                        "This folder is empty,\nPress Ctrl + C to cancel..." +
                        colorama.Style.RESET_ALL)
              valid = False
              while valid == False:
                  filename = input(colorama.Style.RESET_ALL + termdes + " ")
                  try:
                      with open(filename) as f:
                          None
                      valid = True
                  except:
                      print(colorama.Fore.RED + "\033[1mError: file: '" +
                            filename + "' not found.")
                      valid = False
              try:
                  print("------")
                  print(colorama.Fore.RED +
                        "Are you sure you want to delete this file?" +
                        colorama.Style.RESET_ALL)
                  print("Location name: '" + RED +
                        filename + colorama.Style.RESET_ALL + "'")
                  valid = False
                  while valid == False:
                      print("------")
                      print(RED +
                            "'y' - (yes)\nOR\n'n' - (no)" +
                            colorama.Style.RESET_ALL)
                      print("------")
                      choice = input(colorama.Style.RESET_ALL + termdes + " ")
                      choice = choice.strip()
                      if choice.lower() == "y" or choice.lower() == "n":
                          valid = True
                      else:
                          print(colorama.Fore.RED +
                                "Invalid answer. Use (y/n) to respond." +
                                colorama.Style.RESET_ALL)
                  if choice.lower() == "y":
                      if filename.strip(" ") not in systemdirs:
                          try:
                              os.remove(filename)
                              print(colorama.Fore.LIGHTGREEN_EX +
                                    "File successfully deleted: '" + filename + "'" +
                                    colorama.Style.RESET_ALL)
                              print("------")
                          except:
                              print()
                              print(colorama.Fore.RED + "An error occurred" +
                                    colorama.Style.RESET_ALL)
                      else:
                          print(colorama.Fore.RED + "This file is a system file, and therefore cannot be removed." +
                                    colorama.Style.RESET_ALL)
    
              except:
                  print()
                  print(colorama.Fore.RED + "An error occurred" +
                        colorama.Style.RESET_ALL)
          except KeyboardInterrupt:
              print()
              print(colorama.Fore.RED + "Cancelling operation..." +
                    colorama.Style.RESET_ALL)
              print("------")
        elif currentCommand == "view":
          try:
              old = os.getcwd()
              print("------")
              print("Which" + RED + " file " +
                    colorama.Style.RESET_ALL +
                    "would you like to view, \nUsing the system path?")
              getdirectory()
              print("------")
              lista()
              folderscan()
              print()
              valid = False
              while valid == False:
                  selection = input(colorama.Style.RESET_ALL + termdes + " ")
                  try:
                      with open(selection) as f:
                          None
                      f.close()
                      valid = True
                  except:
                      try:
                          os.chdir(selection)
                          os.chdir(old)
                          valid = True
                      except:
                          print(colorama.Fore.RED + "\033[1mError: location '" +
                                selection + "' not found.")
                          valid = False
              print("------")
              filename = selection
              try:
                  os.system(os.getcwd() + "/" + filename)
              except:
                  webbrowser.open_new(os.getcwd() + "/" + filename)
    
          except KeyboardInterrupt:
              print()
              print(colorama.Fore.RED + "Cancelling operation..." +
                    colorama.Style.RESET_ALL)
              print("------")
        elif currentCommand == "dir":
          try:
              getdirectory()
              print("------")
              lista()
              folderscan()
              print("------")
          except KeyboardInterrupt:
              print()
              print(colorama.Fore.RED + "Cancelling operation..." +
                    colorama.Style.RESET_ALL)
        elif currentCommand == "notes":
          old = os.getcwd()
          os.chdir(home_directory + "/Notes")
    
          print("------")
          try:
              if notes == 0:
                  print("You don't have any notes. Let's make one!")
              else:
                  if notes == 1:
                      print("You currently have" +
                            RED + " 1 " +
                            colorama.Style.RESET_ALL + "note.")
                      print("------")
                  else:
                      print("You currently have " +
                            RED + str(notes) +
                            colorama.Style.RESET_ALL + " notes.")
              print(
                  "Would you like to do?...\n\n" +
                  RED + "1)" +
                  colorama.Style.RESET_ALL + " Create a note\n-- OR --\n" +
                  RED + "2)" +
                  colorama.Style.RESET_ALL +
                  " Append (add) to a note?\n\nPlease use numbers (1 or 2) to answer."
              )
              valid = False
              while valid == False:
                  choice = input(colorama.Style.RESET_ALL + termdes + " ")
                  choice = str(choice)
                  answers = ["1", "2"]
                  if choice not in answers:
                      print("Please use the" + RED +
                            " numbers 1 or 2 " + colorama.Style.RESET_ALL +
                            "to answer.")
                      valid = False
    
                  elif choice == "1" or choice == "2":
                      valid = True
                      break
              ###########################################################
              if choice == "1":
                  print("------")
                  print("What is the title of the note? ")
                  valid = False
                  while valid == False:
                      title = input(colorama.Style.RESET_ALL + termdes + " ")
                      if title.strip(" ") == "":
                          print("The name of the note cannot be blank!")
                          valid = False
                      else:
                          valid = True
                          break
    
                  filename = title + ".txt"
                  f = open(filename, "w")
                  print("------")
                  print(
                      LIGHTGREEN +
                      "Please write the note data below, and press Ctrl + C to save and exit."
                      + colorama.Style.RESET_ALL)
                  counter = 0
                  while True:
                      try:
                          counter = counter + 1
                          line = input(colorama.Style.RESET_ALL + RED +
                                       str(counter) + ": " +
                                       colorama.Style.RESET_ALL)
                          f.write(line + "\n")
                      except KeyboardInterrupt:
                          try:
                              print("---")
                              f.close()
                              print(colorama.Fore.LIGHTGREEN_EX +
                                    "File successfully saved - '" +
                                    RED + filename +
                                    colorama.Fore.LIGHTGREEN_EX + "'" +
                                    colorama.Style.RESET_ALL +
                                    "\nFind your file in the folder 'Notes'")
                              print("------")
                              os.chdir(old)
                              break
                          except:
                              print()
                              print(colorama.Fore.RED +
                                    "File failed to save..." +
                                    colorama.Style.RESET_ALL)
                              print("------")
                              os.chdir(old)
                              break
              if choice != "1":
                  print("------")
                  print("Which note would you like to add to?")
                  dir = os.getcwd()
                  dlist = dir.split("/")
                  print("------")
                  if str(dlist[-1]) != "":
                      print("Directory: '" + RED +
                            str(dlist[-1]) + colorama.Style.RESET_ALL + "'")
                  else:
                      print("Directory: '" + RED +
                            "replit" + colorama.Style.RESET_ALL + "'")
    
                  print("------")
                  listfiles()
                  if notes == 0:
                      print(colorama.Fore.LIGHTBLACK_EX +
                            "This folder is empty,\nPress Ctrl+C to cancel..." +
                            colorama.Style.RESET_ALL)
                  print("------")
                  valid = False
                  while valid == False:
                      filename = input(colorama.Style.RESET_ALL + termdes + " ")
                      try:
                          with open(filename) as f:
                              None
                          valid = True
                      except:
                          print(colorama.Fore.RED + "\033[1mError: file: '" +
                                filename + "' not found.")
                          valid = False
                  with open(filename) as f:
                      contents = f.readlines()
                  f.close()
                  print("------")
                  print("The contents of '" + RED +
                        filename + colorama.Style.RESET_ALL + "':")
                  print("------")
                  for line in contents:
                      print(line, end="")
                      time.sleep(0.02)
                  print()
                  print("------")
                  f = open(filename, "a")
                  print(
                      LIGHTGREEN +
                      "Please write the note data below, and press Ctrl + C to save and exit."
                      + colorama.Style.RESET_ALL)
                  counter = 0
                  while True:
                      try:
                          counter = counter + 1
                          line = input(colorama.Style.RESET_ALL + RED +
                                       str(counter) + ": " +
                                       colorama.Style.RESET_ALL)
                          f.write(line + "\n")
                      except KeyboardInterrupt:
                          try:
                              print("---")
                              f.close()
                              print(colorama.Fore.LIGHTGREEN_EX +
                                    "File successfully saved - '" +
                                    RED + filename +
                                    colorama.Fore.LIGHTGREEN_EX + "'" +
                                    colorama.Style.RESET_ALL +
                                    "\nFind your file in the folder 'Notes'")
                              print("------")
                              os.chdir(old)
                              break
                          except:
                              print()
                              print(colorama.Fore.RED +
                                    "File failed to save..." +
                                    colorama.Style.RESET_ALL)
                              print("------")
                              os.chdir(old)
                              break
    
          except KeyboardInterrupt:
              print()
              print(colorama.Fore.RED + "Cancelling operation..." +
                    colorama.Style.RESET_ALL)
              print("------")
              os.chdir(old)
        elif currentCommand == "play":
          old = os.getcwd()
          os.chdir(home_directory)
          os.chdir("Games")
          try:
              print("------")
              print("T.E.S.S Games vRPIos")
              print(f"{RED}Note:{reset} you can quit any running game with [CTRL] [C].")
              print("Which " + RED + "game" + reset + " would you like to run?")
              print(RED + "Be careful when running code from sources you don't trust.\nMake sure you know what you're doing!" + reset)
              getdirectory()
              print("------")
              listfiles()
              DIR = os.getcwd()
              amount = len([
                  name for name in os.listdir(DIR)
                  if os.path.isfile(os.path.join(DIR, name))
              ])
              if amount == 0:
                  print(colorama.Fore.LIGHTBLACK_EX +
                        "This folder is empty,\nPress Ctrl+C to cancel..." +
                        colorama.Style.RESET_ALL)
              print("------")
              print(f"{RED}WARNING:{reset} file names are case sensitive! Please include any capital letters, symbols and file extentions.")
              print(f"{RED}(e.g: 'file.py', or 'music.mp3'){reset}")
    
              valid = False
              while valid == False:
                  filename = input(colorama.Style.RESET_ALL + termdes + " ")
                  try:
                      with open(filename) as f:
                          None
                      valid = True
                  except:
                      print(colorama.Fore.RED + "\033[1mError: file: '" +
                            filename + "' not found.")
                      valid = False
    
              print("------")
              try:
                  exec(open(filename).read())
    
              except KeyboardInterrupt:
                  print()
                  print(colorama.Fore.RED + "Ending session..." +
                        colorama.Style.RESET_ALL)
                  print("------")
                  os.chdir(old)
    
              except:
                  print(colorama.Fore.RED +
                        "An error ocurred whilst running the file: '" +
                        str(filename) + "'")
                  print("------")
              os.chdir(old)
    
          except KeyboardInterrupt:
              print()
              print(colorama.Fore.RED + "Cancelling operation..." +
                    colorama.Style.RESET_ALL)
              os.chdir(old)
          os.chdir(old)
          print("------")
        elif currentCommand == "apps":
          old = os.getcwd()
          os.chdir(home_directory)
          os.chdir("Apps")
          try:
              print("------")
              print(f"{RED}Note:{reset} you can quit any running application with [CTRL] [C].")
              print("Which " + RED + "app" + reset + " would you like to run?")
              print(RED + "Be careful when running code from sources you don't trust.\nMake sure you know what you're doing!" + reset)
              getdirectory()
              print("------")
              listfiles()
              DIR = os.getcwd()
              amount = len([
                  name for name in os.listdir(DIR)
                  if os.path.isfile(os.path.join(DIR, name))
              ])
              if amount == 0:
                  print(colorama.Fore.LIGHTBLACK_EX +
                        "This folder is empty,\nPress Ctrl+C to cancel..." +
                        colorama.Style.RESET_ALL)
              print("------")
              print(f"{RED}WARNING:{reset} file names are case sensitive! Please include any capital letters, symbols and file extentions.")
              print(f"{RED}(e.g: 'file.py', or 'music.mp3'){reset}")

              valid = False
              while valid == False:
                  filename = input(colorama.Style.RESET_ALL + termdes + " ")
                  try:
                      with open(filename) as f:
                          None
                      valid = True
                  except:
                      print(colorama.Fore.RED + "\033[1mError: file: '" +
                            filename + "' not found.")
                      valid = False

              print("------")
              try:
                  exec(open(filename).read())

              except KeyboardInterrupt:
                  print()
                  print(colorama.Fore.RED + "Ending session..." +
                        colorama.Style.RESET_ALL)
                  print("------")
                  os.chdir(old)

              except:
                  print(colorama.Fore.RED +
                        "An error ocurred whilst running the file: '" +
                        str(filename) + "'")
                  print("------")
              os.chdir(old)

          except KeyboardInterrupt:
              print()
              print(colorama.Fore.RED + "Cancelling operation..." +
                    colorama.Style.RESET_ALL)
              os.chdir(old)
          os.chdir(old)
          print("------")
        elif currentCommand == ("systeminfo"):
            print(" ")
            system_status()
            print(" ")
            continue
        elif currentCommand == ("employeelist"):
            print(" ")
            slowType("Accessing Tahmasbi Industries Database...", .02)
            time.sleep(1)
            print(" ")
            print(fake.name())
            print(fake.address())
            print(" ")
            continue
        elif currentCommand == ("internetspeedtest"):
          print(" ")
          download_speed, upload_speed = perform_speed_test()
          print(" ")
          print("Download Speed: {:.2f} Mbps".format(download_speed))
          print("Upload Speed: {:.2f} Mbps".format(upload_speed))
          print(" ")
          continue
        elif currentCommand == ("clock"):
          clock()
          continue
        elif currentCommand == ("credits"):
            slowType("Creators Of The Tahmasbi Industries Electromagnetic Supercomputer System:", .05)
            print(" ")
            slowType("The Main 3:", .05)
            print("Creator: Aidan Tahmasbi")
            print("Contributor: TriTechX")
            print("Contributor: Aidan Chui")
            print(" ")
            slowType("Game Creators:", .05)
            print("Buckshot Roulette: DrDevil4")
            print("Tic Tac Toe: TriTechX")
            print("BlackJack: Xytrophico and TriTechX")
            print(" ")
            slowType("Testers:", .05)
            print("Ben West")
            print("Harry Hall-Bennet")
            print("Adam Shahzaman")
            print("Jarod Wright")
            print("Correy Morris")
            print("Noah Sherlock-Daley")
            print(" ")
        elif currentCommand == "error":
            print(dingusmunch)
        else:
            print(" ")
            print("Command not found.")
            print(" ")
            continue
except KeyboardInterrupt:
    slowType("Keyboard Interrupt Detected.", .02)
    time.sleep(2)
    print(" ")
    slowType("T.E.S.S Shutting Down...", .02)
    print(" ")
    time.sleep(2)
    slowType("Returning Back To Debian TTY...", .02)
    print(" ")
    time.sleep(2)
    print("Done!")
    print(" ")
    exit()
except:
    dirback()
    os.system("clear")
    print(ERRORLOGO)
    print(" ")
    slowType("Something went wrong and T.E.S.S had to shut down.", .02)
    exit()
#-------------------------------------------------------------------------------------------------------------------
#The End?