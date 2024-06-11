class Player:
    def __init__(
        self, id, name, position, height, training, speed, goals, assists, injured
    ):
        self.id = id
        self.name = name
        self.position = position
        self.height = height
        self.training = training
        self.speed = speed
        self.goals = goals
        self.assists = assists
        self.injured = injured

    def calculate_score(self):
        if self.injured:
            return 0
        if self.height < 5 or self.height > 9:
            return 0
        if self.training < 6:
            return 0
        weights = [0.1, 0.2, 0.1, 0.3, 0.3]
        scores = [self.height, self.training, self.speed, self.goals, self.assists]
        return sum([weight * score for weight, score in zip(weights, scores)])


players = [
    Player(1, "Player1", "midfielder", 7, 8, 6, 4, 3, False),
    Player(2, "Player2", "midfielder", 6, 7, 5, 3, 2, False),
    Player(3, "Player3", "midfielder", 8, 9, 7, 5, 4, False),
    Player(4, "Player4", "midfielder", 5, 6, 4, 2, 1, False),
    Player(5, "Player5", "forward", 7, 8, 6, 4, 3, False),
    Player(6, "Player6", "forward", 6, 7, 5, 3, 2, False),
    Player(7, "Player7", "forward", 8, 9, 7, 5, 4, False),
    Player(8, "Player8", "forward", 5, 6, 4, 2, 1, False),
    Player(9, "Player9", "midfielder", 7, 8, 6, 4, 3, True),
    Player(10, "Player10", "forward", 6, 7, 5, 3, 2, True),
]

for player in players:
    print(
        f"Player {player.id}: {player.name}, Position: {player.position}, Height: {player.height}, Training: {player.training}, Speed: {player.speed}, Goals: {player.goals}, Assists: {player.assists}, Injured: {player.injured}"
    )

while True:
    player_id = int(
        input("Enter the player id to change score or injury status (0 to continue): ")
    )
    if player_id == 0:
        break
    player = next((player for player in players if player.id == player_id), None)
    if player:
        category = input(
            "Enter the category to change (height, training, speed, goals, assists, injured): "
        )
        if category == "injured":
            player.injured = not player.injured
        else:
            score = int(input("Enter the new score: "))
            if category == "height":
                player.height = score
            elif category == "training":
                player.training = score
            elif category == "speed":
                player.speed = score
            elif category == "goals":
                player.goals = score
            elif category == "assists":
                player.assists = score

midfielders = [
    player
    for player in players
    if player.position == "midfielder" and not player.injured
]
forwards = [
    player for player in players if player.position == "forward" and not player.injured
]

midfielders.sort(key=lambda player: player.calculate_score(), reverse=True)
forwards.sort(key=lambda player: player.calculate_score(), reverse=True)

selected_midfielders = midfielders[:3]
selected_forwards = forwards[:2]

print("Selected Midfielders:")
for player in selected_midfielders:
    print(f"Player {player.id}: {player.name}, Score: {player.calculate_score()}")

print("Selected Forwards:")
for player in selected_forwards:
    print(f"Player {player.id}: {player.name}, Score: {player.calculate_score()}")
