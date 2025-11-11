from System.SlowTypeFunction import slowType
#------------------------------------------------------------------------------------------------------------------
#Caesar Cipher
def caesar_cipher(encoded_message, shift):

  decoded_message = ""

  for char in encoded_message:
    if char == " ":
        decoded_message += " "
    else:
      char_code = ord(char)
      shifted_code = char_code + shift

      if shifted_code < 65:
          shifted_code += 26

      elif shifted_code > 90:
          shifted_code -= 26

      decoded_char = chr(shifted_code)
      decoded_message += decoded_char

  print(f"Output Message: {decoded_message}")
print(" ")
slowType("Caesar Cipher For T.E.S.S OS vRPIos", .02)
print(" ")
print("Assuming you are using English ABC Alphabet In ASCII")
print(" ")
shift = int(input("Enter the shift: "))
print(" ")
encoded_message = input("Input Message: ").upper()
print(" ")
caesar_cipher(encoded_message, shift)
print(" ")