import random
import time

# Define the symbols and their probabilities
symbols = ["🍒", "🍊", "🍋", "🍇", "🔔", "7️⃣"]
weights = [5, 4, 3, 2, 1, 1]  # Higher weight means more common


def spin_reels():
    """Simulates spinning the slot machine reels."""
    return [random.choices(symbols, weights=weights)[0] for _ in range(3)]


def check_win(result):
    """Checks the result for winning combinations and payouts."""
    if result[0] == result[1] == result[2]:
        # Three of a kind
        if result[0] == "7️⃣":
            return "Jackpot! (100x bet)"
        else:
            return "Three of a kind! (5x bet)"
    elif result[0] == result[1] or result[1] == result[2]:
        # Two of a kind
        return "Two of a kind! (2x bet)"
    else:
        return "No win. Try again!"


def play_game():
    """Main game loop."""
    balance = 100  # Starting balance

    while balance > 0:
        print(f"Current balance: ${balance}")
        bet = int(input("Enter your bet: $"))
        if bet > balance:
            print("You don't have enough balance.")
            continue

        result = spin_reels()
        print("Spinning...")
        time.sleep(1)  # Add some suspense
        print(f"Result: {result[0]} | {result[1]} | {result[2]}")

        win_message = check_win(result)
        print(win_message)

        if "Jackpot" in win_message:
            balance += bet * 100
        elif "Three of a kind" in win_message:
            balance += bet * 5
        elif "Two of a kind" in win_message:
            balance += bet * 2
        else:
            balance -= bet

    print("Game over! You ran out of money.")


if __name__ == "__main__":
    play_game()
