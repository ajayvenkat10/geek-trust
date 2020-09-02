from collections import defaultdict


class Kingdom:

    def __init__(self, name, animal):

        self.name = name
        self.animal = animal
        self.animal_frequency_map = self.calculateFrequencyMap()

    def calculateFrequencyMap(self):

        frequency_map = defaultdict(int)

        for letter in self.animal:
            frequency_map[letter] += 1

        return frequency_map
