# -*- coding: utf-8 -*-
"""
Created on Mon Mar 27 23:50:37 2023

@author: Danial.Riaz
"""

class CaesarCipher:
    def __init__(self, shift):
        self.shift = shift % 26

    def encrypt(self, message):
        """Encrypt the message using the Caesar cipher"""
        chars = list(message)
        for i in range(len(chars)):
            if chars[i].isalpha():
                if chars[i].islower():
                    chars[i] = chr((ord(chars[i]) - ord('a') + self.shift) % 26 + ord('a'))
                else:
                    chars[i] = chr((ord(chars[i]) - ord('A') + self.shift) % 26 + ord('A'))
        return ''.join(chars)

    def decrypt(self, message):
        """Decrypt the message using the Caesar cipher"""
        chars = list(message)
        for i in range(len(chars)):
            if chars[i].isalpha():
                if chars[i].islower():
                    chars[i] = chr((ord(chars[i]) - ord('a') - self.shift) % 26 + ord('a'))
                else:
                    chars[i] = chr((ord(chars[i]) - ord('A') - self.shift) % 26 + ord('A'))
        return ''.join(chars)



