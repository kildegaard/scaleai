import random

class Civilization:
    def __init__(self, name, magic_affinity, military_strength, cultural_influence):
        self.name = name
        self.magic_affinity = magic_affinity
        self.military_strength = military_strength
        self.cultural_influence = cultural_influence
        self.resources = 100
        self.allies = []
        self.enemies = []

    def form_alliance(self, other):
        self.allies.append(other)
        other.allies.append(self)

    def wage_war(self, other):
        if self.military_strength > other.military_strength:
            self.resources += 50
            other.resources -= 50
            self.enemies.append(other)
            other.enemies.append(self)
        else:
            self.resources -= 50
            other.resources += 50
            self.enemies.append(other)
            other.enemies.append(self)

    def trade_resources(self, other):
        if self.resources > 50 and other.resources > 50:
            self.resources -= 25
            other.resources += 25
            self.allies.append(other)
            other.allies.append(self)

    def __str__(self):
        return f"{self.name}: Magic Affinity - {self.magic_affinity}, Military Strength - {self.military_strength}, Cultural Influence - {self.cultural_influence}, Resources - {self.resources}"

def mythical_world(civilizations, years):
    chronicle = []
    for year in range(years):
        for civilization in civilizations:
            if random.random() < 0.1:  # 10% chance of a magical storm
                civilization.resources -= 20
                chronicle.append(f"Year {year}: A magical storm hit {civilization.name}!")
            if random.random() < 0.05:  # 5% chance of a volcanic eruption
                civilization.resources -= 50
                chronicle.append(f"Year {year}: A volcanic eruption hit {civilization.name}!")
            if random.random() < 0.05:  # 5% chance of a celestial alignment
                civilization.resources += 50
                chronicle.append(f"Year {year}: A celestial alignment blessed {civilization.name}!")
            if random.random() < 0.1:  # 10% chance of forming an alliance
                other = random.choice(civilizations)
                if other != civilization and other not in civilization.allies and other not in civilization.enemies:
                    civilization.form_alliance(other)
                    chronicle.append(f"Year {year}: {civilization.name} formed an alliance with {other.name}!")
            if random.random() < 0.05:  # 5% chance of waging war
                other = random.choice(civilizations)
                if other != civilization and other not in civilization.allies and other not in civilization.enemies:
                    civilization.wage_war(other)
                    chronicle.append(f"Year {year}: {civilization.name} waged war against {other.name}!")
            if random.random() < 0.1:  # 10% chance of trading resources
                other = random.choice(civilizations)
                if other != civilization and other not in civilization.enemies:
                    civilization.trade_resources(other)
                    chronicle.append(f"Year {year}: {civilization.name} traded resources with {other.name}!")
    for civilization in civilizations:
        chronicle.append(str(civilization))
    return chronicle

# Example usage
civilizations = [
    Civilization("Atlantis", 80, 70, 90),
    Civilization("Eldrador", 90, 60, 80),
    Civilization("Nefaria", 70, 80, 70),
    Civilization("Arcania", 60, 90, 60),
]

chronicle = mythical_world(civilizations, 100)
for event in chronicle:
    print(event)