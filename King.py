class King:

    kingdoms_captured = []

    def __init__(self, name, kingdom_name, cipher, minimum_kingdoms_to_capture):
        self.name = name 
        self.kingdom_name = kingdom_name
        self.cipher = cipher
        self.MIN_REQUIRED_TO_BE_RULER = minimum_kingdoms_to_capture

    def addKingdom(self, kingdom_name):
        self.kingdoms_captured.append(kingdom_name)

    def kingdomsRuled(self):
        if(len(self.kingdoms_captured) >= self.MIN_REQUIRED_TO_BE_RULER):
            self.kingdoms_captured.insert(0, self.kingdom_name)

        else:
            self.kingdoms_captured = ["NONE"]

        return self.kingdoms_captured

    
