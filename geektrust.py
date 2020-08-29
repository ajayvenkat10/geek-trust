import sys
from collections import defaultdict

NUMBER_OF_ALPHABETS = 26
ASCII_VAL_OF_A = 65

kingdom_animal_map = {"SPACE": "GORILLA",
                      "LAND": "PANDA",
                      "WATER": "OCTOPUS",
                      "ICE": "MAMMOTH",
                      "AIR": "OWL",
                      "FIRE": "DRAGON"}

character_frequencies_map = defaultdict(dict)


def calculateFrequencyMap(animal):

    frequency_map = defaultdict(int)

    for letter in animal:
        frequency_map[letter] += 1

    return frequency_map


def obtainAnimalCharacterFrequencies():

    for kingdom in kingdom_animal_map:
        character_frequencies_map[kingdom] = calculateFrequencyMap(
            kingdom_animal_map[kingdom])


def decryptLetter(letter, key):

    return chr(((ord(letter) - key - ASCII_VAL_OF_A) % NUMBER_OF_ALPHABETS) + ASCII_VAL_OF_A)


def decryptCaesarCipher(key, ciphertext):

    plaintext = ""
    frequency_dict = defaultdict(int)

    for letter in ciphertext:
        intended_letter = decryptLetter(letter, key)
        frequency_dict[intended_letter] += 1
        plaintext += intended_letter

    return frequency_dict


def isCaptureSuccessful(kingdom_frequency_map, decrypted_frequency_map):

    for char in kingdom_frequency_map:
        if(decrypted_frequency_map[char] < kingdom_frequency_map[char]):
            return False

    return True


def solveGoldenCrown(input_file):

    kingdoms_captured = []

    with open(input_file) as in_file:
        inputs = in_file.readlines()

        for input in inputs:
            input = input.split()
            kingdom = input[0]
            message = ''.join(input[1:])

            decryption_frequencies_map = decryptCaesarCipher(
                len(kingdom_animal_map[kingdom]),
                message)

            if(isCaptureSuccessful(character_frequencies_map[kingdom], decryption_frequencies_map)):
                kingdoms_captured.append(kingdom)
                if(len(kingdoms_captured) == 3):
                    break

        if(len(kingdoms_captured) == 3):
            kingdoms_captured.insert(0, "SPACE")

        else:
            kingdoms_captured = ["NONE"]

    in_file.close()

    print(* kingdoms_captured)


def main():

    obtainAnimalCharacterFrequencies()
    solveGoldenCrown(sys.argv[1])


if __name__ == "__main__":

    main()
