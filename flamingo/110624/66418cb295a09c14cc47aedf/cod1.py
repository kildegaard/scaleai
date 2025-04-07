import random

class Civilization:
    def __init__(self, name, magic_affinity, military_strength, cultural_influence):
        self.name = name
        self.magic_affinity = magic_affinity
        self.military_strength = military_strength
        self.cultural_influence = cultural_influence
        self.allies = []
        self.resources = 100

    def form_alliance(self, civilization):
        self.allies.append(civilization)

    def wage_war(self, civilization):
        if self.military_strength > civilization.military_strength:
            civilization.resources -= 20
            self.resources += 20
            return f"{self.name} has defeated {civilization.name} in a war!"
        else:
            self.resources -= 20
            civilization.resources += 20
            return f"{civilization.name} has defeated {self.name} in a war!"

    def trade_resources(self, civilization):
        trade_amount = random.randint(1, 10)
        self.resources -= trade_amount
        civilization.resources += trade_amount
        return f"{self.name} has traded {trade_amount} resources with {civilization.name}!"

class MythicalWorld:
    def __init__(self):
        self.civilizations = []
        self.world_events = []

    def simulate_century(self):
        for civilization in self.civilizations:
            civilization.resources += 10
            if random.random() < 0.1:
                self.world_events.append(f"{civilization.name} has discovered a new technology!")
                civilization.magic_affinity += 10
                civilization.military_strength += 10
                civilization.cultural_influence += 10
            if random.random() < 0.2:
                self.world_events.append(f"{civilization.name} has experienced a natural disaster!")
                civilization.resources -= 20
                civilization.magic_affinity -= 10
                civilization.military_strength -= 10
                civilization.cultural_influence -= 10
        for i in range(len(self.civilizations)):
            for j in range(i+1, len(self.civilizations)):
                if random.random() < 0.1:
                    self.world_events.append(self.civilizations[i].wage_war(self.civilizations[j]))
                elif random.random() < 0.2:
                    self.world_events.append(self.civilizations[i].trade_resources(self.civilizations[j]))
                elif random.random() < 0.3:
                    self.civilizations[i].form_alliance(self.civilizations[j])
                    self.world_events.append(f"{self.civilizations[i].name} and {self.civilizations[j].name} have formed an alliance!")

    def simulate_history(self, centuries):
        for century in range(centuries):
            self.simulate_century()
        for civilization in self.civilizations:
            print(f"{civilization.name} has a magic affinity of {civilization.magic_affinity}, a military strength of {civilization.military_strength}, a cultural influence of {civilization.cultural_influence}, and {civilization.resources} resources.")
        print("World Events:")
        for event in self.world_events:
            print(event)

def mythical_world():
    world = MythicalWorld()
    world.civilizations.append(Civilization("Civilization 1", 50, 50, 50))
    world.civilizations.append(Civilization("Civilization 2", 60, 40, 30))
    world.civilizations.append(Civilization("Civilization 3", 40, 60, 20))
    world.simulate_history(10)

mythical_world()