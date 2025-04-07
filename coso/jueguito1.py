import random
import time

# Define the symbols and their corresponding weights (probabilities)
symbols = ["Cherry", "Lemon", "Orange", "Plum", "Bell", "Bar", "Seven"]
weights = [5, 4, 3, 2, 1, 0.5, 0.1]  # Higher weight = higher probability


def spin_reels():
    """Simulates spinning the reels and returns a list of three symbols."""
    return [random.choices(symbols, weights=weights)[0] for _ in range(3)]


def display_reels(reels):
    """Prints the reels in a visually appealing format."""
    print("-----")
    for symbol in reels:
        print(f"| {symbol} |")
    print("-----")


def check_win(reels):
    """Checks if the reels resulted in a win and returns the payout multiplier."""
    if reels[0] == reels[1] == reels[2]:
        # All three symbols match
        if reels[0] == "Seven":
            return 100  # Jackpot!
        else:
            return 5  # Regular win
    elif reels[0] == reels[1] or reels[1] == reels[2]:
        # Two adjacent symbols match
        return 2  # Small win
    else:
        return 0  # No win


def play_game():
    """Main game loop."""
    balance = 100  # Starting balance

    while balance > 0:
        print(f"Balance: ${balance}")
        bet = int(input("Enter your bet: "))
        if bet > balance:
            print("Not enough balance.")
            continue

        balance -= bet
        reels = spin_reels()
        display_reels(reels)
        winnings = bet * check_win(reels)
        balance += winnings

        if winnings > 0:
            print(f"You won ${winnings}!")
        else:
            print("Try again.")

    print("Game over! You ran out of money.")


if __name__ == "__main__":
    play_game()
