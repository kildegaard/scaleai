from collections import deque

N = int(input())
P = list(map(int, input().split()))
D = int(input())

days = []
for _ in range(D):
    L, R, V = map(int, input().split())
    days.append((L, R, V))

evacuated = 0
for L, R, V in days:
    # Calculate the total number of residents in the foggy districts
    total_residents = sum(P[L - 1 : R])

    # Evacuate as many residents as possible
    evacuated_today = min(total_residents, V)
    evacuated += evacuated_today

    # If there are still remaining residents, move them to the district with the smallest number of residents
    remaining_residents = total_residents - evacuated_today
    P[L - 1] += remaining_residents
    for i in range(L, R):
        P[i] = 0

print(evacuated)
