from abc import ABC, abstractmethod


# Resource classes
class Resource(ABC):
    def __init__(self, quantity, production_rate, consumption_rate):
        self.quantity = quantity
        self.production_rate = production_rate
        self.consumption_rate = consumption_rate

    def update_quantity(self):
        self.quantity += self.production_rate - self.consumption_rate

    def add(self, amount):
        self.quantity += amount

    def remove(self, amount):
        if self.quantity >= amount:
            self.quantity -= amount
        else:
            print("Insufficient resources.")


class Wood(Resource):
    def __init__(self, quantity=100, production_rate=10, consumption_rate=0):
        super().__init__(quantity, production_rate, consumption_rate)


class Stone(Resource):
    def __init__(self, quantity=100, production_rate=5, consumption_rate=0):
        super().__init__(quantity, production_rate, consumption_rate)


class Food(Resource):
    def __init__(self, quantity=100, production_rate=10, consumption_rate=5):
        super().__init__(quantity, production_rate, consumption_rate)


class Gold(Resource):
    def __init__(self, quantity=100, production_rate=5, consumption_rate=0):
        super().__init__(quantity, production_rate, consumption_rate)


# Structure classes
class Structure(ABC):
    def __init__(self, cost, construction_time, production_bonus):
        self.cost = cost
        self.construction_time = construction_time
        self.production_bonus = production_bonus
        self.level = 0

    @abstractmethod
    def build(self, resources):
        pass

    @abstractmethod
    def upgrade(self, resources):
        pass

    @abstractmethod
    def demolish(self, resources):
        pass


class Farm(Structure):
    def __init__(
        self,
        cost={"wood": 50, "stone": 20, "food": 0, "gold": 10},
        construction_time=2,
        production_bonus={"food": 5},
    ):
        super().__init__(cost, construction_time, production_bonus)

    def build(self, resources):
        if all(resources[key].quantity >= value for key, value in self.cost.items()):
            for key, value in self.cost.items():
                resources[key].remove(value)
            self.level += 1
            print("Farm built.")
        else:
            print("Insufficient resources.")

    def upgrade(self, resources):
        if self.level > 0:
            upgrade_cost = {key: value * self.level for key, value in self.cost.items()}
            if all(
                resources[key].quantity >= value for key, value in upgrade_cost.items()
            ):
                for key, value in upgrade_cost.items():
                    resources[key].remove(value)
                self.level += 1
                print("Farm upgraded.")
            else:
                print("Insufficient resources.")
        else:
            print("Structure not built.")

    def demolish(self, resources):
        if self.level > 0:
            for key, value in self.production_bonus.items():
                resources[key].production_rate -= value * self.level
            self.level = 0
            print("Farm demolished.")
        else:
            print("Structure not built.")


class Barracks(Structure):
    def __init__(
        self,
        cost={"wood": 100, "stone": 50, "food": 0, "gold": 20},
        construction_time=3,
        production_bonus={"gold": 5},
    ):
        super().__init__(cost, construction_time, production_bonus)

    def build(self, resources):
        if all(resources[key].quantity >= value for key, value in self.cost.items()):
            for key, value in self.cost.items():
                resources[key].remove(value)
            self.level += 1
            print("Barracks built.")
        else:
            print("Insufficient resources.")

    def upgrade(self, resources):
        if self.level > 0:
            upgrade_cost = {key: value * self.level for key, value in self.cost.items()}
            if all(
                resources[key].quantity >= value for key, value in upgrade_cost.items()
            ):
                for key, value in upgrade_cost.items():
                    resources[key].remove(value)
                self.level += 1
                print("Barracks upgraded.")
            else:
                print("Insufficient resources.")
        else:
            print("Structure not built.")

    def demolish(self, resources):
        if self.level > 0:
            for key, value in self.production_bonus.items():
                resources[key].production_rate -= value * self.level
            self.level = 0
            print("Barracks demolished.")
        else:
            print("Structure not built.")


class TownHall(Structure):
    def __init__(
        self,
        cost={"wood": 200, "stone": 100, "food": 0, "gold": 50},
        construction_time=5,
        production_bonus={"wood": 5, "stone": 5, "food": 5, "gold": 5},
    ):
        super().__init__(cost, construction_time, production_bonus)

    def build(self, resources):
        if all(resources[key].quantity >= value for key, value in self.cost.items()):
            for key, value in self.cost.items():
                resources[key].remove(value)
            self.level += 1
            print("Town Hall built.")
        else:
            print("Insufficient resources.")

    def upgrade(self, resources):
        if self.level > 0:
            upgrade_cost = {key: value * self.level for key, value in self.cost.items()}
            if all(
                resources[key].quantity >= value for key, value in upgrade_cost.items()
            ):
                for key, value in upgrade_cost.items():
                    resources[key].remove(value)
                self.level += 1
                print("Town Hall upgraded.")
            else:
                print("Insufficient resources.")
        else:
            print("Structure not built.")

    def demolish(self, resources):
        if self.level > 0:
            for key, value in self.production_bonus.items():
                resources[key].production_rate -= value * self.level
            self.level = 0
            print("Town Hall demolished.")
        else:
            print("Structure not built.")


# Game class
class Game:
    def __init__(self):
        self.resources = {
            "wood": Wood(),
            "stone": Stone(),
            "food": Food(),
            "gold": Gold(),
        }
        self.structures = {
            "farm": Farm(),
            "barracks": Barracks(),
            "town hall": TownHall(),
        }
        self.turn = 0

    def update_resources(self):
        for resource in self.resources.values():
            resource.update_quantity()

    def check_victory_conditions(self):
        if self.resources["gold"].quantity >= 1000:
            print("You have won the game! (Gold Victory)")
            return True
        elif self.structures["town hall"].level >= 5:
            print("You have won the game! (Town Hall Victory)")
            return True
        return False

    def play_turn(self):
        self.turn += 1
        print(f"Turn {self.turn}:")
        self.update_resources()
        print("Resources:")
        for key, value in self.resources.items():
            print(f"{key.capitalize()}: {value.quantity}")
        action = input("Enter an action (build, upgrade, demolish, pass): ")
        if action == "build":
            structure = input(
                "Enter a structure to build (farm, barracks, town hall): "
            )
            if structure in self.structures:
                self.structures[structure].build(self.resources)
            else:
                print("Invalid structure.")
        elif action == "upgrade":
            structure = input(
                "Enter a structure to upgrade (farm, barracks, town hall): "
            )
            if structure in self.structures:
                self.structures[structure].upgrade(self.resources)
            else:
                print("Invalid structure.")
        elif action == "demolish":
            structure = input(
                "Enter a structure to demolish (farm, barracks, town hall): "
            )
            if structure in self.structures:
                self.structures[structure].demolish(self.resources)
            else:
                print("Invalid structure.")
        elif action == "pass":
            pass
        else:
            print("Invalid action.")
        if self.check_victory_conditions():
            return False
        return True


game = Game()
while game.play_turn():
    pass
