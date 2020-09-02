from Kingdom import *
from collections import defaultdict


class GoldenCrown:

    NUMBER_OF_ALPHABETS = 26
    ASCII_VAL_OF_A = 65

    def __init__(self, kingdoms_list, animals_list):

        self.kingdoms = kingdoms_list
        self.animals = animals_list
        self.kingdom_name_object_map = defaultdict(Kingdom)
        self.preprocessing()

    def preprocessing(self):

        for i in range(len(self.kingdoms)):
            kingdom = Kingdom(self.kingdoms[i], self.animals[i])
            self.kingdom_name_object_map[kingdom.name] = kingdom

    def decryptLetter(self, letter, key):

        return chr(((ord(letter) - key - self.ASCII_VAL_OF_A) %
                    self.NUMBER_OF_ALPHABETS) + self.ASCII_VAL_OF_A)

    def decryptCaesarCipher(self, key, ciphertext):

        plaintext = ""
        frequency_dict = defaultdict(int)

        for letter in ciphertext:
            intended_letter = self.decryptLetter(letter, key)
            frequency_dict[intended_letter] += 1
            plaintext += intended_letter

        return frequency_dict

    def isCaptureSuccessful(self, kingdom_name, message):

        decrypted_frequency_map = self.decryptCaesarCipher(
            len(self.kingdom_name_object_map[kingdom_name].animal), message)

        kingdom_frequency_map = self.kingdom_name_object_map[kingdom_name].animal_frequency_map

        for char in kingdom_frequency_map:
            if(decrypted_frequency_map[char] < kingdom_frequency_map[char]):
                return False

        return True
