class Harbor:
    def __init__(self, name, location):
        self.name = name
        self.location = location
        self.schedule = {}

    def is_time_slot_available(self, time_slot):
        return time_slot not in self.schedule

    def assign_time_slot(self, ship, time_slot):
        if self.is_time_slot_available(time_slot):
            self.schedule[time_slot] = ship
            return True
        else:
            return False


class Ship:
    def __init__(self, id, personnel, cargo):
        self.id = id
        self.personnel = personnel
        self.cargo = cargo


class System:
    def __init__(self):
        self.ships = {}
        self.harbors = {}

    def add_ship(self, id, personnel, cargo):
        if cargo not in ['cars', 'food', 'livestock', 'oil']:
            raise ValueError('Invalid cargo type')
        self.ships[id] = Ship(id, personnel, cargo)

    def add_harbor(self, name, location):
        self.harbors[name] = Harbor(name, location)

    def assign_harbor_time_slot(self, ship_id, harbor_name, time_slot):
        if ship_id not in self.ships:
            raise ValueError('Ship not found')
        if harbor_name not in self.harbors:
            raise ValueError('Harbor not found')
        return self.harbors[harbor_name].assign_time_slot(self.ships[ship_id], time_slot)

    def get_ship_info(self, ship_id):
        if ship_id not in self.ships:
            raise ValueError('Ship not found')
        ship = self.ships[ship_id]
        return f'Ship ID: {ship.id}, Personnel: {ship.personnel}, Cargo: {ship.cargo}'

    def get_harbor_schedule(self, harbor_name):
        if harbor_name not in self.harbors:
            raise ValueError('Harbor not found')
        return self.harbors[harbor_name].schedule


# Usage example:

system = System()
system.add_ship(1, 10, 'cars')
system.add_ship(2, 20, 'food')
system.add_harbor('Harbor 1', 'New York')
system.add_harbor('Harbor 2', 'Los Angeles')

print(system.get_ship_info(1))
print(system.assign_harbor_time_slot(1, 'Harbor 1', '10:00'))
print(system.assign_harbor_time_slot(2, 'Harbor 1', '10:00'))  # Returns False
print(system.get_harbor_schedule('Harbor 1'))