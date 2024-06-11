from abc import ABC, abstractmethod


# Resource classes
class Resource:
    def __init__(self, quantity, production_rate, consumption_rate):
        self.quantity = quantity
        self.production_rate = production_rate
        self.consumption_rate = consumption_rate

    def update_quantity(self):
        self.quantity += self.production_rate - self.consumption_rate

    def add_quantity(self, amount):
        self.quantity += amount

    def remove_quantity(self, amount):
        if amount > self.quantity:
            raise ValueError("Insufficient resources")
        self.quantity -= amount


class Wood(Resource):
    def __init__(self, quantity=100, production_rate=10, consumption_rate=0):
        super().__init__(quantity, production_rate, consumption_rate)


class Stone(Resource):
    def __init__(self, quantity=50, production_rate=5, consumption_rate=0):
        super().__init__(quantity, production_rate, consumption_rate)


class Food(Resource):
    def __init__(self, quantity=200, production_rate=20, consumption_rate=10):
        super().__init__(quantity, production_rate, consumption_rate)


class Gold(Resource):
    def __init__(self, quantity=0, production_rate=0, consumption_rate=0):
        super().__init__(quantity, production_rate, consumption_rate)


# Structure classes
class Structure(ABC):
    @abstractmethod
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
        cost={"wood": 50, "stone": 20, "food": 0, "gold": 0},
        construction_time=2,
        production_bonus={"food": 10},
    ):
        super().__init__(cost, construction_time, production_bonus)

    def build(self, resources):
        for resource, amount in self.cost.items():
            resources[resource].remove_quantity(amount)
        self.level += 1

    def upgrade(self, resources):
        if self.level < 1:
            raise ValueError("Structure not built yet")
        for resource, amount in self.cost.items():
            resources[resource].remove_quantity(amount * self.level)
        self.level += 1

    def demolish(self, resources):
        if self.level < 1:
            raise ValueError("Structure not built yet")
        for resource, amount in self.production_bonus.items():
            resources[resource].production_rate -= amount * self.level
        self.level = 0


class Sawmill(Structure):
    def __init__(
        self,
        cost={"wood": 20, "stone": 10, "food": 0, "gold": 0},
        construction_time=2,
        production_bonus={"wood": 5},
    ):
        super().__init__(cost, construction_time, production_bonus)

    def build(self, resources):
        for resource, amount in self.cost.items():
            resources[resource].remove_quantity(amount)
        self.level += 1

    def upgrade(self, resources):
        if self.level < 1:
            raise ValueError("Structure not built yet")
        for resource, amount in self.cost.items():
            resources[resource].remove_quantity(amount * self.level)
        self.level += 1

    def demolish(self, resources):
        if self.level < 1:
            raise ValueError("Structure not built yet")
        for resource, amount in self.production_bonus.items():
            resources[resource].production_rate -= amount * self.level
        self.level = 0


class Mine(Structure):
    def __init__(
        self,
        cost={"wood": 50, "stone": 10, "food": 0, "gold": 0},
        construction_time=3,
        production_bonus={"stone": 5, "gold": 2},
    ):
        super().__init__(cost, construction_time, production_bonus)

    def build(self, resources):
        for resource, amount in self.cost.items():
            resources[resource].remove_quantity(amount)
        self.level += 1

    def upgrade(self, resources):
        if self.level < 1:
            raise ValueError("Structure not built yet")
        for resource, amount in self.cost.items():
            resources[resource].remove_quantity(amount * self.level)
        self.level += 1

    def demolish(self, resources):
        if self.level < 1:
            raise ValueError("Structure not built yet")
        for resource, amount in self.production_bonus.items():
            resources[resource].production_rate -= amount * self.level
        self.level = 0


# Game class
class Game:
    def __init__(self):
        self.resources = {
            "wood": Wood(),
            "stone": Stone(),
            "food": Food(),
            "gold": Gold(),
        }
        self.structures = {"farm": Farm(), "sawmill": Sawmill(), "mine": Mine()}
        self.turn = 0

    def update_resources(self):
        for resource in self.resources.values():
            resource.update_quantity()

    def check_victory_conditions(self):
        # Victory condition 1: 1000 gold
        if self.resources["gold"].quantity >= 1000:
            return True
        # Victory condition 2: 100 food, 100 wood, and 100 stone
        if (
            self.resources["food"].quantity >= 100
            and self.resources["wood"].quantity >= 100
            and self.resources["stone"].quantity >= 100
        ):
            return True
        return False

    def play_turn(self):
        self.turn += 1
        self.update_resources()
        print(f"Turn {self.turn}:")
        print("Resources:")
        for resource, amount in self.resources.items():
            print(f"{resource.capitalize()}: {amount.quantity}")
        action = input("Enter action (build, upgrade, demolish, pass): ")
        if action == "build":
            structure = input("Enter structure to build (farm, sawmill, mine): ")
            self.structures[structure].build(self.resources)
        elif action == "upgrade":
            structure = input("Enter structure to upgrade (farm, sawmill, mine): ")
            self.structures[structure].upgrade(self.resources)
        elif action == "demolish":
            structure = input("Enter structure to demolish (farm, sawmill, mine): ")
            self.structures[structure].demolish(self.resources)
        if self.check_victory_conditions():
            print("Victory!")
            return False
        return True


# Main loop
game = Game()
while game.play_turn():
    pass
