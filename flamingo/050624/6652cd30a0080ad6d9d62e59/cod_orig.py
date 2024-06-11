import random
import json
from collections import defaultdict

roles = {"waiters": 10, "cleaners": 10, "chefs": 5, "receptionists": 3, "concierge": 10}

shifts = ["morning", "afternoon", "night"]

weekly_schedule = {
    day: {shift: {role: [] for role in roles} for shift in shifts} for day in range(7)
}

staff = {
    role: [f"{role[:-1]}_{i+1}" for i in range(count)] for role, count in roles.items()
}


def assign_shifts():
    for role, employees in staff.items():
        for day in range(7):
            random.shuffle(employees)
            morning_shift = employees[: len(employees) // 2]
            night_shift = employees[len(employees) // 2 :][: len(employees) // 2]
            afternoon_shift = employees[len(employees) // 2 :][len(employees) // 2 :]

            # Assign shifts to the schedule
            weekly_schedule[day]["morning"][role].extend(morning_shift)
            weekly_schedule[day]["afternoon"][role].extend(afternoon_shift)
            weekly_schedule[day]["night"][role].extend(night_shift)


def limit_shifts_per_week():
    for role, employees in staff.items():
        shift_counts = defaultdict(int)
        for day in range(7):
            for shift in shifts:
                for emp in weekly_schedule[day][shift][role]:
                    shift_counts[emp] += 1

        for emp, count in shift_counts.items():
            if count > 5:
                days_worked = [day for day in range(7) if emp in sum(weekly_schedule[day][shift][role] for shift in shifts)]
                extra_days = random.sample(days_worked, count - 5)
                for day in extra_days:
                    for shift in shifts:
                        if emp in weekly_schedule[day][shift][role]:
                            weekly_schedule[day][shift][role].remove(emp)
                            break


assign_shifts()
limit_shifts_per_week()


def print_schedule_json():
    print(json.dumps(weekly_schedule, indent=2))


print_schedule_json()
