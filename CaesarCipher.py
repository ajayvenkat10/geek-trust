from Ciphers import *
from collections import defaultdict

class CaesarCipher(Ciphers):

    ASCII_VAL_OF_A = 65
    NUMBER_OF_ALPHABETS = 26

    def decryptionLogicForLetters(self, letter, key):
        return chr(((ord(letter) - key - self.ASCII_VAL_OF_A) %
                    self.NUMBER_OF_ALPHABETS) + self.ASCII_VAL_OF_A)

    def decryptCiphertext(self, key, ciphertext):

        plaintext = ""
        frequency_dict = defaultdict(int)

        for letter in ciphertext:
            intended_letter = self.decryptionLogicForLetters(letter, key)
            frequency_dict[intended_letter] += 1
            plaintext += intended_letter

        return frequency_dict

    def getCipherName(self):
        return "Caesar Cipher"
