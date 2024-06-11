def validate_evacuation_inputs(num_players, player_strengths, num_requests):
    if not isinstance(num_players, int) or num_players <= 0:
        raise ValueError("Number of players must be a positive integer.")
    if not isinstance(player_strengths, list) or not all(
        isinstance(p, int) for p in player_strengths
    ):
        raise ValueError("Player strengths must be a list of integers.")
    if not isinstance(num_requests, int) or num_requests <= 0:
        raise ValueError("Number of evacuation requests must be a positive integer.")


def display_evacuation_statistics(
    total_evacuated, evacuation_history, average_strength
):
    print("Total evacuated players:", total_evacuated)
    print("Evacuation Details:")
    for i, (request, players_evacuated) in enumerate(evacuation_history):
        print(f"Request {i + 1}: {request}, Evacuated Players: {players_evacuated}")
    print("Average strength of evacuated players:", average_strength)


def calculate_evacuation_plan(num_players, player_strengths, requests):
    validate_evacuation_inputs(num_players, player_strengths, len(requests))

    num_requests = len(requests)

    dp = [[0] * (num_requests + 1) for _ in range(num_players + 1)]

    evacuation_history = [[] for _ in range(num_requests)]

    for j in range(1, num_requests + 1):
        req_players, max_strength_limit = requests[j - 1]
        for i in range(1, num_players + 1):
            if i >= req_players:
                current_sum = sum(player_strengths[i - req_players : i])
                if current_sum <= max_strength_limit:
                    dp[i][j] = max(dp[i][j], dp[i - req_players][j - 1] + current_sum)
                    if dp[i][j] > dp[i - 1][j]:
                        evacuation_history[j - 1] = (
                            requests[j - 1],
                            player_strengths[i - req_players : i],
                        )
            dp[i][j] = max(dp[i][j], dp[i - 1][j])

    total_evacuated = max(dp[num_players])

    evacuated_players = [
        player
        for _, players_evacuated in evacuation_history
        for player in players_evacuated
    ]
    total_strength_evacuated = sum(evacuated_players)
    average_strength_evacuated = (
        total_strength_evacuated / len(evacuated_players) if evacuated_players else 0
    )

    return total_evacuated, evacuation_history, average_strength_evacuated


if __name__ == "__main__":
    num_players = int(input("Enter number of players: "))
    player_strengths = list(map(int, input("Enter player strengths: ").split()))

    requests = []
    num_requests = int(input("Enter number of evacuation requests: "))
    for _ in range(num_requests):
        req_players, max_strength_limit = map(int, input().split())
        requests.append((req_players, max_strength_limit))

    total_evacuated, evacuation_history, average_strength_evacuated = (
        calculate_evacuation_plan(num_players, player_strengths, requests)
    )

    display_evacuation_statistics(
        total_evacuated, evacuation_history, average_strength_evacuated
    )
