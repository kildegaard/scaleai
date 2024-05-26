from collections import deque

N = int(input())
P = list(map(int, input().split()))
D = int(input())

days = []
for i in range(D):
    L, R, V = map(int, input().split())
    days.append((L, R, V))

residents = deque([(i, P[i - 1]) for i in range(1, N + 1)])

evacuated = 0
for L, R, V in days:
    temp = deque()
    while residents and residents[0][0] < L:
        temp.append(residents.popleft())
    while residents and residents[0][0] <= R:
        district, people = residents.popleft()
        evacuate = min(V, people)
        evacuated += evacuate
        V -= evacuate
        people -= evacuate
        if people > 0:
            temp.append((district, people))
    while temp:
        residents.appendleft(temp.pop())

print(evacuated)
