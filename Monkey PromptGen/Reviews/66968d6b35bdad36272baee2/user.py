import random
import time
import os


def generate_data(size):
    """Generates a list of exactly 50 random numbers and 50 texts."""
    data = []
    for _ in range(size // 2):
        data.append(str(random.randint(1, 100)))
        data.append(random.choice(["apple", "banana", "orange", "grape", "watermelon"]))
    random.shuffle(data)
    return data


def clear_screen():
    """Clears the console screen."""
    os.system("cls" if os.name == "nt" else "clear")


def display_matrix(data, rows, cols):
    """Displays the data in a matrix format."""
    matrix = [data[i * cols : (i + 1) * cols] for i in range(rows)]
    for row in matrix:
        print(" ".join(f"{item:<10}" for item in row))

    clear_screen()
    get_user_input(rows, cols)


def get_user_input(rows, cols):
    """Gets user input and stores it in a list."""
    print(f"Enter the elements you remember (row by row, separated by spaces):")
    user_data = []
    for _ in range(rows):
        row_input = input().split()
        if len(row_input) != cols:
            print(f"Invalid input. Please enter {cols} values for each row.")
            return None
        user_data.extend(row_input)
    calculate_score(user_data)


def calculate_score(user_data):
    """Calculates the percentage of correct entries."""
    data = generate_data(len(user_data))  # Regenerate data based on user input length
    total_items = min(len(data), len(user_data))
    correct_count = sum(1 for i in range(total_items) if data[i] == user_data[i])
    score = (correct_count / total_items) * 100 if total_items > 0 else 0
    print("Score:", score)
    """Displays the result based on the score."""
    if score == 100:
        print("Genius!")
    elif score >= 70:
        print("Good memory!")
    elif score >= 50:
        print("Average memory.")
    else:
        print("Need improvement.")


def main():
    """Main function to run the memory game."""
    data = generate_data(100)

    print("Welcome to the Memory Game!")
    print("Select difficulty:")
    print("1. Low")
    print("2. Medium")
    print("3. High")

    while True:
        choice = input("Enter your choice (1-3): ")
        if choice in ["1", "2", "3"]:
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

    if choice == "1":
        rows, cols = 3, 3
    elif choice == "2":
        rows, cols = 5, 5
    else:
        rows, cols = 8, 8

    clear_screen()  # Clear the screen before displaying the matrix
    display_matrix(data[: rows * cols], rows, cols)


if __name__ == "__main__":
    main()
