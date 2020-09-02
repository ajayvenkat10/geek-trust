import sys
from collections import defaultdict

MIN_REQUIRED_TO_BE_RULER = 3


class GoldenCrown:

    NUMBER_OF_ALPHABETS = 26
    ASCII_VAL_OF_A = 65

    kingdom_animal_map = {"SPACE": "GORILLA",
                          "LAND": "PANDA",
                          "WATER": "OCTOPUS",
                          "ICE": "MAMMOTH",
                          "AIR": "OWL",
                          "FIRE": "DRAGON"}

    character_frequencies_map = defaultdict(dict)

    def __init__(self):
        self.obtainAnimalCharacterFrequencies()

    def calculateFrequencyMap(self, animal):

        frequency_map = defaultdict(int)

        for letter in animal:
            frequency_map[letter] += 1

        return frequency_map

    def obtainAnimalCharacterFrequencies(self):

        for kingdom in self.kingdom_animal_map:
            self.character_frequencies_map[kingdom] = self.calculateFrequencyMap(
                self.kingdom_animal_map[kingdom])

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

    def isCaptureSuccessful(self, kingdom, message):

        decrypted_frequency_map = self.decryptCaesarCipher(
            len(self.kingdom_animal_map[kingdom]), message)

        kingdom_frequency_map = self.character_frequencies_map[kingdom]

        for char in kingdom_frequency_map:
            if(decrypted_frequency_map[char] < kingdom_frequency_map[char]):
                return False

        return True


def solveGoldenCrown(input_file):

    kingdoms_captured = []

    goldenCrown = GoldenCrown()

    with open(input_file) as in_file:
        inputs = in_file.readlines()

        for input in inputs:
            input = input.split()
            kingdom = input[0]
            message = ''.join(input[1:])

            if(goldenCrown.isCaptureSuccessful(kingdom, message)):
                kingdoms_captured.append(kingdom)

        if(len(kingdoms_captured) >= MIN_REQUIRED_TO_BE_RULER):
            kingdoms_captured.insert(0, "SPACE")

        else:
            kingdoms_captured = ["NONE"]

    in_file.close()

    print(* kingdoms_captured)


def main():

    solveGoldenCrown(sys.argv[1])


if __name__ == "__main__":

    main()
