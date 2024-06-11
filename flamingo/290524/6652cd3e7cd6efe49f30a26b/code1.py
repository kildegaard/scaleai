import tkinter as tk  # Import the tkinter library and assign it a shorter alias 'tk' for convenience
from tkinter import (
    messagebox,
)  # Import the messagebox module from tkinter to display messages


def button_click(btn):  # Method to handle the click event of a button
    global current_player  # Access the global variable 'current_player' to modify it inside this method

    # Check if the button is empty and the game is not over
    if btn["text"] == "" and not game_over:
        # If the current player is 'X', mark the button as 'X' and switch the current player to 'O'
        if current_player == "X":
            btn["text"] = "X"
            current_player = "O"
        # If the current player is 'O', mark the button as 'O' and switch the current player to 'X'
        else:
            btn["text"] = "O"
            current_player = "X"
        check_winner()  # Check if there's a winner after this move


def check_winner():  # Method to check if there's a winner or a draw
    global game_over  # Access the global variable 'game_over' to modify it inside this method

    # Check rows for a winner
    for i in range(3):
        if (
            buttons[i][0]["text"]
            == buttons[i][1]["text"]
            == buttons[i][2]["text"]
            != ""
        ):
            # If a winner is found, highlight the winning buttons and set 'game_over' to True
            buttons[i][0].config(bg="green")
            buttons[i][1].config(bg="green")
            buttons[i][2].config(bg="green")
            game_over = True

    # Check columns for a winner
    for i in range(3):
        if (
            buttons[0][i]["text"]
            == buttons[1][i]["text"]
            == buttons[2][i]["text"]
            != ""
        ):
            # If a winner is found, highlight the winning buttons and set 'game_over' to True
            buttons[0][i].config(bg="green")
            buttons[1][i].config(bg="green")
            buttons[2][i].config(bg="green")
            game_over = True

    # Check the main diagonal for a winner
    if buttons[0][0]["text"] == buttons[1][1]["text"] == buttons[2][2]["text"] != "":
        # If a winner is found, highlight the winning buttons and set 'game_over' to True
        buttons[0][0].config(bg="green")
        buttons[1][1].config(bg="green")
        buttons[2][2].config(bg="green")
        game_over = True

    # Check the other diagonal for a winner
    if buttons[0][2]["text"] == buttons[1][1]["text"] == buttons[2][0]["text"] != "":
        # If a winner is found, highlight the winning buttons and set 'game_over' to True
        buttons[0][2].config(bg="green")
        buttons[1][1].config(bg="green")
        buttons[2][0].config(bg="green")
        game_over = True

    # Check if it's a draw (all buttons are filled and no winner)
    if (
        all(buttons[i][j]["text"] != "" for i in range(3) for j in range(3))
        and not game_over
    ):
        game_over = True
        messagebox.showinfo(
            "Tic Tac Toe", "It's a draw!"
        )  # Display a message for a draw
        reset_game()  # Reset the game

    # If the game is over, display a message for the winner and reset the game
    if game_over:
        winner = "O" if current_player == "X" else "X"  # Determine the winner
        messagebox.showinfo(
            "Tic Tac Toe", f"Player {winner} wins!"
        )  # Display a message for the winner
        reset_game()  # Reset the game


def reset_game():  # Method to reset the game
    global current_player, game_over  # Access the global variables 'current_player' and 'game_over' to modify them inside this method
    current_player = "X"  # Reset the current player to 'X'
    game_over = False  # Reset the game over status to False
    for i in range(3):
        for j in range(3):
            # Reset each button's text and background color
            buttons[i][j].config(text="", bg="SystemButtonFace")


app = tk.Tk()  # Create a new tkinter application
app.title("Tic Tac Toe")  # Set the title of the application window

current_player = "X"  # Initialize the current player to 'X'
game_over = False  # Initialize the game over status to False

# Create a 3x3 grid of buttons
buttons = [
    [
        tk.Button(
            app,
            text="",
            font="Arial 20",
            width=5,
            height=2,
            command=lambda i=i, j=j: button_click(buttons[i][j]),
        )
        for j in range(3)
    ]
    for i in range(3)
]

# Layout the buttons in a grid
for i in range(3):
    for j in range(3):
        buttons[i][j].grid(row=i, column=j)

app.mainloop()  # Start the application's main event loop
