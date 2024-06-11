# Hospital data
hospital = {
    "Department A": {
        "Floor 1": {
            "Room 101": {
                "room_number": "101",
                "area": 20,
                "price": 500,
                "available": True,
            },
            "Room 102": {
                "room_number": "102",
                "area": 30,
                "price": 600,
                "available": False,
            },
            "Room 103": {
                "room_number": "103",
                "area": 25,
                "price": 550,
                "available": True,
            },
        },
        "Floor 2": {
            "Room 201": {
                "room_number": "201",
                "area": 35,
                "price": 700,
                "available": True,
            },
            "Room 202": {
                "room_number": "202",
                "area": 20,
                "price": 500,
                "available": False,
            },
        },
    },
    "Department B": {
        "Floor 1": {
            "Room 101": {
                "room_number": "101",
                "area": 30,
                "price": 650,
                "available": True,
            },
            "Room 102": {
                "room_number": "102",
                "area": 25,
                "price": 550,
                "available": False,
            },
        },
        "Floor 2": {
            "Room 201": {
                "room_number": "201",
                "area": 40,
                "price": 800,
                "available": True,
            },
            "Room 202": {
                "room_number": "202",
                "area": 30,
                "price": 650,
                "available": False,
            },
        },
    },
}


def get_available_rooms_by_department(department):
    available_rooms = []
    for floor, rooms in hospital.get(department, {}).items():
        for room, details in rooms.items():
            if details["available"]:
                available_rooms.append(room)
    return available_rooms


def get_available_rooms_by_department_and_floor(department, floor):
    available_rooms = []
    for room, details in hospital.get(department, {}).get(floor, {}).items():
        if details["available"]:
            available_rooms.append(room)
    return available_rooms


def get_available_rooms_by_price_range(min_price, max_price):
    available_rooms = []
    for department, floors in hospital.items():
        for floor, rooms in floors.items():
            for room, details in rooms.items():
                if details["available"] and min_price <= details["price"] <= max_price:
                    available_rooms.append(
                        {"department": department, "floor": floor, "room": room}
                    )
    return available_rooms


# Test the functions
print(get_available_rooms_by_department("Department A"))
print(get_available_rooms_by_department_and_floor("Department A", "Floor 1"))
print(get_available_rooms_by_price_range(500, 700))
