from CaesarCipher import *
from collections import defaultdict


class Kingdom:

    def __init__(self, name, animal):

        self.name = name
        self.animal = animal
        self.animal_frequency_map = self.calculateFrequencyMap()
        self.key = len(animal)

    def calculateFrequencyMap(self):

        frequency_map = defaultdict(int)

        for letter in self.animal:
            frequency_map[letter] += 1

        return frequency_map

    def isCaptureSuccessful(self, message, cipher):

        decrypted_frequency_map = cipher.decryptCiphertext(self.key, message)

        for char in self.animal_frequency_map:
            if(decrypted_frequency_map[char] < self.animal_frequency_map[char]):
                return False

        return True
        
