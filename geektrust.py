import sys
from collections import defaultdict
from GoldenCrown import *

MIN_REQUIRED_TO_BE_RULER = 3
RULER = "SPACE"

def solveGoldenCrown(input_file):

    kingdoms_list = ["SPACE", "LAND", "WATER", "ICE", "AIR", "FIRE"]
    animals_list = ["GORILLA", "PANDA",
                    "OCTOPUS", "MAMMOTH", "OWL", "DRAGON"]
    
    goldenCrown = GoldenCrown(kingdoms_list, animals_list)

    kingdoms_captured = []

    with open(input_file) as in_file:
        inputs = in_file.readlines()

        for input in inputs:
            input = input.split()
            kingdom_name = input[0]
            message = ''.join(input[1:])

            if(goldenCrown.isCaptureSuccessful(kingdom_name, message)):
                kingdoms_captured.append(kingdom_name)

    in_file.close()

    if(len(kingdoms_captured) >= MIN_REQUIRED_TO_BE_RULER):
        kingdoms_captured.insert(0, RULER)

    else:
        kingdoms_captured = ["NONE"]

    return kingdoms_captured

def main():

    ruled_kingdoms = solveGoldenCrown(sys.argv[1])

    print(* ruled_kingdoms)


if __name__ == "__main__":

    main()
