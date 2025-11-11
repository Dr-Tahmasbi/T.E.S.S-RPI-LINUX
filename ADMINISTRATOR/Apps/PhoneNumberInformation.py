import time
import phonenumbers
from phonenumbers import carrier
from phonenumbers import geocoder
from phonenumbers import timezone
from System.SlowTypeFunction import slowType
#------------------------------------------------------------------------------------------------------------------
#Phone Number Information
def phonenumber_information():
  try:
    print(" ")
    slowType("T.E.S.S OS Telephone Geolocator vRPIos", .02)
    print(" ")
    number = input("Enter a phone number (with regional code): ")
    number = phonenumbers.parse(number)
    print(" ")
    print("Searching...")
    time.sleep(1)
    print(" ")
    print(f'Carrier: {carrier.name_for_number(number, "en")}')
    print(f'Timezone: {timezone.time_zones_for_number(number)}')
    print(f'Location: {geocoder.description_for_number(number, "en")}')
    print(" ")
  except:
    print(" ")
    print("Number not found.")
    print(" ")
phonenumber_information()