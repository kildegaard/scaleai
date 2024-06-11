def validate_evacuation_inputs(num_players, player_strengths, num_requests):
    """
    Validates the inputs for the evacuation plan calculation.

    Args:
        num_players (int): The number of players.
        player_strengths (list): A list of integers representing the strengths of the players.
        num_requests (int): The number of evacuation requests.

    Raises:
        ValueError: If the inputs are not valid.
    """
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
    """
    Displays the statistics of the evacuation plan.

    Args:
        total_evacuated (int): The total number of players evacuated.
        evacuation_history (list): A list of tuples containing the evacuation details.
        average_strength (float): The average strength of the evacuated players.
    """
    print("Total evacuated players:", total_evacuated)
    print("Evacuation Details:")
    for i, (request, players_evacuated) in enumerate(evacuation_history):
        print(f"Request {i + 1}: {request}, Evacuated Players: {players_evacuated}")
    print("Average strength of evacuated players:", average_strength)


def calculate_evacuation_plan(num_players, player_strengths, requests):
    """
    Calculates the evacuation plan based on the given inputs.

    Args:
        num_players (int): The number of players.
        player_strengths (list): A list of integers representing the strengths of the players.
        requests (list): A list of tuples containing the evacuation requests.

    Returns:
        tuple: A tuple containing the total number of players evacuated, the evacuation history, and the average strength of the evacuated players.
    """
    # Validate the inputs
    validate_evacuation_inputs(num_players, player_strengths, len(requests))

    # Get the number of requests
    num_requests = len(requests)

    # Initialize a 2D table to store the maximum strength that can be evacuated for each subproblem
    dp = [[0] * (num_requests + 1) for _ in range(num_players + 1)]

    # Initialize a list to store the evacuation history
    evacuation_history = [[] for _ in range(num_requests)]

    # Iterate over each request
    for j in range(1, num_requests + 1):
        # Get the current request
        req_players, max_strength_limit = requests[j - 1]

        # Iterate over each player
        for i in range(1, num_players + 1):
            # If the current player can be evacuated in the current request
            if i >= req_players:
                # Calculate the sum of the strengths of the players that can be evacuated
                current_sum = sum(player_strengths[i - req_players : i])

                # If the sum of the strengths does not exceed the maximum strength limit
                if current_sum <= max_strength_limit:
                    # Update the maximum strength that can be evacuated for the current subproblem
                    dp[i][j] = max(dp[i][j], dp[i - req_players][j - 1] + current_sum)

                    # If the current solution is better than the previous one, update the evacuation history
                    if dp[i][j] > dp[i - 1][j]:
                        evacuation_history[j - 1] = (
                            requests[j - 1],
                            player_strengths[i - req_players : i],
                        )

            # Update the maximum strength that can be evacuated for the current subproblem
            dp[i][j] = max(dp[i][j], dp[i - 1][j])

    # Get the total number of players evacuated
    total_evacuated = max(dp[num_players])

    # Get the evacuated players
    evacuated_players = [
        player
        for _, players_evacuated in evacuation_history
        for player in players_evacuated
    ]

    # Calculate the total strength of the evacuated players
    total_strength_evacuated = sum(evacuated_players)

    # Calculate the average strength of the evacuated players
    average_strength_evacuated = (
        total_strength_evacuated / len(evacuated_players) if evacuated_players else 0
    )

    # Return the total number of players evacuated, the evacuation history, and the average strength of the evacuated players
    return total_evacuated, evacuation_history, average_strength_evacuated


if __name__ == "__main__":
    # Get the number of players
    num_players = int(input("Enter number of players: "))

    # Get the player strengths
    player_strengths = list(map(int, input("Enter player strengths: ").split()))

    # Get the evacuation requests
    requests = []
    num_requests = int(input("Enter number of evacuation requests: "))
    for _ in range(num_requests):
        req_players, max_strength_limit = map(int, input().split())
        requests.append((req_players, max_strength_limit))

    # Calculate the evacuation plan
    total_evacuated, evacuation_history, average_strength_evacuated = (
        calculate_evacuation_plan(num_players, player_strengths, requests)
    )

    # Display the evacuation statistics
    display_evacuation_statistics(
        total_evacuated, evacuation_history, average_strength_evacuated
    )
