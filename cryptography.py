import random
import time
import sys

def generate_key():
    alphabet = list('abcdefghijklmnopqrstuvwxyz')
    random.shuffle(alphabet)
    return ''.join(alphabet)

def encrypt(key, plaintext):
    result = ''
    for c in plaintext:
        if c.isalpha():
           index = ord(c.lower()) - ord('a')
           result += key[index]
        else:
            result += c
    return result

def decrypt(key, ciphertext):
    result = ''
    for c in ciphertext:
        if c.isalpha():
           index = key.index(c.lower())
           result += chr(index + ord('a'))
        else:
            result += c
    return result

def options(ciphertext, plaintext, x, key):

    if x == 1:
        print(ciphertext)
        time.sleep(1)
        return_to_menu(ciphertext, plaintext, key)
    elif x == 2:
        print(decrypt(key, ciphertext))
        time.sleep(1)
        return_to_menu(ciphertext, plaintext, key)
    elif x == 3:
        print('Generating key...')
        key = generate_key()
        time.sleep(1)
        print('Key generated.')
        print('Encrypting...')
        time.sleep(1)
        ciphertext = encrypt(key, plaintext)
        print('Encrypted.')
        return_to_menu(ciphertext, plaintext, key)
    else:
        print('Exiting...')
        time.sleep(1)
        print('Exiting..')
        time.sleep(1)
        print('Exiting.')
        time.sleep(1)
        sys.exit(200)

def choice():
    print('1. Show encrypted message')
    print('2. Decrypt')
    print('3. Generate new encryption key')
    print('4. Exit')
    x = int(input('Enter a number: '))
    return x
        
def return_to_menu(ciphertext, plaintext, key):
    num = choice()
    options(ciphertext, plaintext, num, key)

def enter_message():
    # take a string input from the user
    plaintext = input("Enter a string: ")

    # check if the input is a string
    if isinstance(plaintext, str):
        plaintext = plaintext.lower()
        return plaintext
    else:
        print("The input is not a string.")
        enter_message()

# Example

def cryptography():
    print('Generating key...')
    key = generate_key()
    time.sleep(1)
    print('Key generated.')

    plaintext = enter_message()
    print('Encrypting...')
    time.sleep(1)
    ciphertext = encrypt(key, plaintext)
    print('Encrypted.')

    return_to_menu(ciphertext, plaintext, key)

cryptography()