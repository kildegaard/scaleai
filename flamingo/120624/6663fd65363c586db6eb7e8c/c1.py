import random
import pandas as pd

# Initialize teams
teams = [f'Team {i}' for i in range(1, 11)]

# Initialize team stats
stats = {team: {'Games Played': 0, 'Games Won': 0, 'Games Lost': 0, 'Games Drawn': 0, 'Goals Scored': 0, 'Goals Against': 0, 'Goal Difference': 0, 'Points': 0} for team in teams}

# Simulate 9 rounds
for round in range(9):
    # Create fixtures for this round
    fixtures = []
    for i in range(5):
        team1 = teams[i]
        team2 = teams[9-i]
        fixtures.append((team1, team2))

    # Simulate matches
    for team1, team2 in fixtures:
        score1 = random.randint(0, 3)
        score2 = random.randint(0, 3)

        stats[team1]['Games Played'] += 1
        stats[team2]['Games Played'] += 1

        stats[team1]['Goals Scored'] += score1
        stats[team2]['Goals Scored'] += score2

        stats[team1]['Goals Against'] += score2
        stats[team2]['Goals Against'] += score1

        stats[team1]['Goal Difference'] = stats[team1]['Goals Scored'] - stats[team1]['Goals Against']
        stats[team2]['Goal Difference'] = stats[team2]['Goals Scored'] - stats[team2]['Goals Against']

        if score1 > score2:
            stats[team1]['Games Won'] += 1
            stats[team2]['Games Lost'] += 1
            stats[team1]['Points'] += 3
        elif score1 < score2:
            stats[team1]['Games Lost'] += 1
            stats[team2]['Games Won'] += 1
            stats[team2]['Points'] += 3
        else:
            stats[team1]['Games Drawn'] += 1
            stats[team2]['Games Drawn'] += 1
            stats[team1]['Points'] += 1
            stats[team2]['Points'] += 1

    # Print table after this round
    print(f'After Round {round+1}:')
    df = pd.DataFrame(stats).T
    print(df)
    print()

# Print final table
print('Final Table:')
df = pd.DataFrame(stats).T
df = df.sort_values(by=['Points', 'Goal Difference'], ascending=False)
print(df)

# Print champion
champion = df.index[0]
print(f'The champion of the tournament is {champion}!')