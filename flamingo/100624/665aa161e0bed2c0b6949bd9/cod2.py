class Ship:
    def __init__(self, id_number, personnel, cargo_type):
        self.id_number = id_number
        self.personnel = personnel
        self.cargo_type = cargo_type

    def __str__(self):
        return f"Ship ID: {self.id_number}, Personnel: {self.personnel}, Cargo Type: {self.cargo_type}"


class Harbor:
    def __init__(self, name, location):
        self.name = name
        self.location = location
        self.time_slots = {f"{hour}:00": None for hour in range(24)}

    def schedule_ship(self, ship, time_slot):
        if self.time_slots[time_slot] is None:
            self.time_slots[time_slot] = ship
            return f"Ship {ship.id_number} scheduled at {time_slot} at {self.name} harbor."
        else:
            return f"Time slot {time_slot} at {self.name} harbor is not available."

    def check_availability(self, time_slot):
        return self.time_slots[time_slot] is None


class ShippingCompany:
    def __init__(self):
        self.ships = {}
        self.harbors = {}

    def add_ship(self, ship):
        self.ships[ship.id_number] = ship

    def add_harbor(self, harbor):
        self.harbors[harbor.name] = harbor

    def schedule_harbor(self, ship_id, harbor_name, time_slot):
        if ship_id in self.ships and harbor_name in self.harbors:
            return self.harbors[harbor_name].schedule_ship(self.ships[ship_id], time_slot)
        else:
            return "Ship or harbor not found."

    def check_harbor_availability(self, harbor_name, time_slot):
        if harbor_name in self.harbors:
            return self.harbors[harbor_name].check_availability(time_slot)
        else:
            return "Harbor not found."


# Example usage:
company = ShippingCompany()

ship1 = Ship("S1", 20, "cars")
ship2 = Ship("S2", 30, "food")

harbor1 = Harbor("Harbor 1", "Location 1")
harbor2 = Harbor("Harbor 2", "Location 2")

company.add_ship(ship1)
company.add_ship(ship2)

company.add_harbor(harbor1)
company.add_harbor(harbor2)

print(company.schedule_harbor("S1", "Harbor 1", "10:00"))  # Schedule ship S1 at Harbor 1 at 10:00
print(company.check_harbor_availability("Harbor 1", "10:00"))  # Check if time slot 10:00 is available at Harbor 1
print(company.schedule_harbor("S2", "Harbor 1", "10:00"))  # Attempt to schedule ship S2 at Harbor 1 at 10:00