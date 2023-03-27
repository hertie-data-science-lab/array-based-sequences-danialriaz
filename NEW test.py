# -*- coding: utf-8 -*-
"""
Created on Mon Mar 27 23:54:44 2023

@author: Danial.Riaz
"""

from NEW_Cipher import CaesarCipher


# Get input from the user
shift = int(input("Enter the shift amount (an integer between 1 and 25): "))
message = input("Enter the message to be encrypted: ")

# Create a CaesarCipher object with the user-specified shift
cipher = CaesarCipher(shift)

# Encrypt and print the message
coded = cipher.encrypt(message)
print("Encrypted message: ", coded)

# Decrypt and print the encrypted message
decoded = cipher.decrypt(coded)
print("Decrypted message: ", decoded)
