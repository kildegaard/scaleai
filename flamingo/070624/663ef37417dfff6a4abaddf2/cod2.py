class Player:
    def __init__(
        self, id, name, position, height, training_days, speed, goals, assists, injured
    ):
        self.id = id
        self.name = name
        self.position = position
        self.height = height
        self.training_days = training_days
        self.speed = speed
        self.goals = goals
        self.assists = assists
        self.injured = injured

    def calculate_score(self):
        if self.injured:
            return 0
        if self.height < 5 or self.height > 9:
            return 0
        if self.training_days < 6:
            return 0
        weights = {
            "height": 0.05,
            "training_days": 0.15,
            "speed": 0.10,
            "goals": 0.30,
            "assists": 0.40,
        }
        score = (
            self.height * weights["height"]
            + self.training_days * weights["training_days"]
            + self.speed * weights["speed"]
            + self.goals * weights["goals"]
            + self.assists * weights["assists"]
        )
        return score


# Define the players
players = [
    Player(1, "John", "Midfielder", 7, 8, 6, 4, 5, False),
    Player(2, "Alice", "Forward", 6, 9, 7, 6, 4, False),
    Player(3, "Bob", "Midfielder", 8, 7, 5, 3, 6, False),
    Player(4, "Charlie", "Forward", 9, 6, 8, 5, 3, True),
    Player(5, "David", "Midfielder", 5, 8, 4, 4, 6, False),
    Player(6, "Eve", "Forward", 7, 9, 6, 7, 5, False),
    Player(7, "Frank", "Midfielder", 6, 7, 5, 3, 4, False),
    Player(8, "George", "Forward", 8, 6, 7, 4, 6, False),
    Player(9, "Hannah", "Midfielder", 9, 8, 8, 6, 7, False),
    Player(10, "Ian", "Forward", 5, 9, 5, 5, 5, False),
]


# Function to update player details
def update_player(players):
    while True:
        print("Enter the player id you want to update (or 'q' to quit):")
        player_id = input()
        if player_id.lower() == "q":
            break
        player_id = int(player_id)
        for player in players:
            if player.id == player_id:
                print(
                    "Enter the attribute you want to update (height, training_days, speed, goals, assists, injured):"
                )
                attribute = input()
                if attribute == "injured":
                    print("Enter True for injured, False otherwise:")
                    value = input().lower() == "true"
                else:
                    print("Enter the new value:")
                    value = int(input())
                setattr(player, attribute, value)
                print("Player updated successfully.")
                return
        print("Player not found.")


# Update player details if needed
print("Do you want to update any player details? (yes/no):")
if input().lower() == "yes":
    update_player(players)

# Calculate scores and select players
midfielders = [
    player
    for player in players
    if player.position == "Midfielder" and not player.injured
]
forwards = [
    player for player in players if player.position == "Forward" and not player.injured
]

midfielders.sort(key=lambda x: x.calculate_score(), reverse=True)
forwards.sort(key=lambda x: x.calculate_score(), reverse=True)

selected_midfielders = midfielders[:3]
selected_forwards = forwards[:2]

print("Selected Midfielders:")
for player in selected_midfielders:
    print(f"{player.name} - Score: {player.calculate_score()}")

print("\nSelected Forwards:")
for player in selected_forwards:
    print(f"{player.name} - Score: {player.calculate_score()}")
