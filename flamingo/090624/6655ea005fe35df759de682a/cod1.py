class Hospital:
    def __init__(self):
        self.data = {
            "department1": {
                "floor1": [
                    {"room_number": 1, "area": 20, "price": 100, "available": True},
                    {"room_number": 2, "area": 30, "price": 150, "available": False},
                ],
                "floor2": [
                    {"room_number": 3, "area": 40, "price": 200, "available": True},
                    {"room_number": 4, "area": 50, "price": 250, "available": False},
                ],
            },
            "department2": {
                "floor1": [
                    {"room_number": 5, "area": 60, "price": 300, "available": True},
                    {"room_number": 6, "area": 70, "price": 350, "available": False},
                ],
                "floor2": [
                    {"room_number": 7, "area": 80, "price": 400, "available": True},
                    {"room_number": 8, "area": 90, "price": 450, "available": False},
                ],
            },
        }

    def get_available_rooms_by_department(self, department):
        available_rooms = []
        for floor in self.data.get(department, {}).values():
            available_rooms.extend([room for room in floor if room["available"]])
        return available_rooms

    def get_available_rooms_by_department_and_floor(self, department, floor):
        available_rooms = [
            room
            for room in self.data.get(department, {}).get(floor, [])
            if room["available"]
        ]
        return available_rooms

    def get_available_rooms_by_price_range(self, min_price, max_price):
        available_rooms = []
        for department in self.data.values():
            for floor in department.values():
                available_rooms.extend(
                    [
                        room
                        for room in floor
                        if room["available"] and min_price <= room["price"] <= max_price
                    ]
                )
        return available_rooms


hospital = Hospital()
print(hospital.get_available_rooms_by_department("department1"))
print(hospital.get_available_rooms_by_department_and_floor("department1", "floor1"))
print(hospital.get_available_rooms_by_price_range(100, 300))
