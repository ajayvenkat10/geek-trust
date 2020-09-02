import sys
from King import *
from Kingdom import *


def calculateNameObjectMap(kingdom_animal_list):

    name_object_map = defaultdict(Kingdom)
    for i in range(len(kingdom_animal_list)):
        kingdom = Kingdom(kingdom_animal_list[i][0], kingdom_animal_list[i][1])
        name_object_map[kingdom.name] = kingdom

    return name_object_map


def solveGoldenCrown(inputs, king, kingdom_name_object_map):

    for input in inputs:
        input = input.split()
        kingdom = kingdom_name_object_map[input[0]]
        message = ''.join(input[1:])

        if(kingdom.isCaptureSuccessful(message, king.cipher)):
            king.addKingdom(kingdom.name)

    return king.kingdomsRuled()


def inputOutput(input_file):

    kingdom_animal_list = [("SPACE", "GORILLA"), ("LAND", "PANDA"), ("WATER", "OCTOPUS"), ("ICE", "MAMMOTH"),
                           ("AIR", "OWL"), ("FIRE", "DRAGON")]

    king = King("Shan", "SPACE", CaesarCipher(), 3)

    kingdom_name_object_map = calculateNameObjectMap(kingdom_animal_list)

    with open(input_file) as in_file:
        inputs = in_file.readlines()

        kingdoms_captured = solveGoldenCrown(
            inputs, king, kingdom_name_object_map)

    in_file.close()

    print(* kingdoms_captured)


def main():

    inputOutput(sys.argv[1])


if __name__ == "__main__":

    main()
