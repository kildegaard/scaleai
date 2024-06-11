import random
import json
from collections import defaultdict

roles = {
    "waiters": 10,
    "cleaners": 10,
    "chefs": 5,
    "receptionists": 3,
    "concierge": 10
}

shifts = ["morning", "afternoon", "night"]

weekly_schedule = {day: {shift: {role: [] for role in roles} for shift in shifts} for day in range(7)}

staff = {role: [f"{role[:-1]}_{i+1}" for i in range(count)] for role, count in roles.items()}

def assign_shifts():
    for role, employees in staff.items():
        random.shuffle(employees)
        for day in range(7):
            day_staff = employees[:5]
            random.shuffle(day_staff)
            morning_shift = day_staff[:len(day_staff)//3]
            afternoon_shift = day_staff[len(day_staff)//3:2*len(day_staff)//3]
            night_shift = day_staff[2*len(day_staff)//3:]
            
            # Assign shifts to the schedule
            weekly_schedule[day]["morning"][role].extend(morning_shift)
            weekly_schedule[day]["afternoon"][role].extend(afternoon_shift)
            weekly_schedule[day]["night"][role].extend(night_shift)
            employees[:] = employees[5:] + employees[:5]

assign_shifts()

def print_schedule_json():
    print(json.dumps(weekly_schedule, indent=2))

print_schedule_json()