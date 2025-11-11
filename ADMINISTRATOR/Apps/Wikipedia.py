import colorama
import wikipedia
from System.SlowTypeFunction import slowType
RED = '\033[31m'
CYAN = '\033[36m'
reset = colorama.Style.RESET_ALL
#------------------------------------------------------------------------------------------------------------------
#Wikipedia In Python
def search_wikipedia():
  try:
    slowType(f"Welcome to {CYAN}Wikipedia{reset} for {RED}T.E.S.S OS{reset}!", .02)
    search = input("What would you like to search for?: ")
    print("---------------------------------------------")
    print(" ")
    print(wikipedia.summary(search.strip(" ")))
    print("---------------------------------------------")
    print(" ")
  except:
    print(" ")
    print("Couldn't find any information")
print(" ")
search_wikipedia()
print(" ")