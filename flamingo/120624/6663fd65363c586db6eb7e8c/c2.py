import random
import itertools

class Team:
    def __init__(self, name):
        self.name = name
        self.games_played = 0
        self.games_won = 0
        self.games_lost = 0
        self.goals_scored = 0
        self.goals_against = 0
        self.points = 0

    def update_stats(self, goals_scored, goals_against):
        self.games_played += 1
        self.goals_scored += goals_scored
        self.goals_against += goals_against
        if goals_scored > goals_against:
            self.games_won += 1
            self.points += 3
        elif goals_scored < goals_against:
            self.games_lost += 1

    def __str__(self):
        goal_diff = self.goals_scored - self.goals_against
        return f"{self.name:8} {self.games_played:2} {self.games_won:2} {self.games_lost:2} {self.goals_scored:2} {self.goals_against:2} {goal_diff:2} {self.points:2}"

def simulate_match(team1, team2):
    goals_team1 = random.randint(0, 3)
    goals_team2 = random.randint(0, 3)
    team1.update_stats(goals_team1, goals_team2)
    team2.update_stats(goals_team2, goals_team1)

def print_table(teams):
    print("Team     GP GW GL GS GA GD PTS")
    for team in teams:
        print(team)

def main():
    teams = [Team(f"Team {i+1}") for i in range(10)]
    schedule = list(itertools.combinations(teams, 2))

    for i in range(9):
        for j in range(5):
            simulate_match(schedule[i*5+j][0], schedule[i*5+j][1])
        print(f"Round {i+1}:")
        print_table(teams)
        print()

    teams.sort(key=lambda team: (team.points, team.goals_scored - team.goals_against), reverse=True)
    print("Final Standings:")
    print_table(teams)
    print(f"The champion is: {teams[0].name}")

if __name__ == "__main__":
    main()