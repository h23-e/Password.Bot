#test.py
# import the string module to bring us all the alphabet
# we call 2 of the lower case alphabet from string module so it loops over it self
# we ask the user to type a word .lower() 
# create an empty variable named elklma elmshfra
# create a loop to catch every single letter on its own 
# inside the loop we create if to check if its a letter or something else like indentation
# pull out each original index 
# make the new index higher in 2 degrees
# make the new index refers to new letter
# print the encrypted word
import string 
 

def decrypt(message,shift):
    alphabet = string.ascii_lowercase

    decrypted_message = ""

    for letter in message:
        if letter.lower() in alphabet:
            original_position = alphabet.index(letter.lower())
            new_position = (original_position - shift) % 26
            decrypted_letter = alphabet[new_position]
            if letter.isupper():
                decrypted_letter = decrypted_letter.upper()

            decrypted_message += decrypted_letter
        else: 
            decrypted_message += letter 

    print(f"Here is the original message \n*****\n {decrypted_message}\n\n******")              

user_message = input("Enter a message: ")    
shift_number = int(input("Enter a shift number: "))

decrypt(user_message,shift_number)