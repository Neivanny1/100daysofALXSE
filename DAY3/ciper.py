
#!/usr/bin/python3
'''
Modules required to cipher
'''
import random
import string

chars = " " + string.punctuation + string.digits + string.ascii_letters
chars = list(chars)
key = chars.copy()
random.shuffle(key)


'''
Fuction to ENCRYPT the plain text
'''
def encrypt():
    plain_text = input("Enter a message to encrypt: ")
    cipher_text = ""

    for letter in plain_text:
        index = chars.index(letter)
        cipher_text += key[index]

    print(f"plain text message  => {plain_text}")
    print(f"cipher text message => {cipher_text}")

'''
Fuction to DECRYPT the cipher text
'''
def decrypt():
  cipher_text = input("Enter a message to encrypt: ")
  plain_text = ""

  for letter in cipher_text:
      index = key.index(letter)
      plain_text += chars[index]

  print(f"cipher text message => {cipher_text}")
  print(f"plain text message  => {plain_text}")

def main():
    encrypt()
    decrypt()
while True:
    main()
    value = int(input("Enter 1 to continue, Any to stop "))
    if value == 1:
      main()
    break    