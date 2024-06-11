import tkinter as tk
from tkinter import messagebox


# Function to handle button click event
def button_click(btn):
    # Access the global variable current_player
    global current_player

    # Check if the button's text is empty and the game is not over
    if btn["text"] == "" and not game_over:
        # If the current player is X, set the button's text to X and switch the current player to O
        if current_player == "X":
            btn["text"] = "X"
            current_player = "O"
        # If the current player is O, set the button's text to O and switch the current player to X
        else:
            btn["text"] = "O"
            current_player = "X"
        # Check if there is a winner after the button click
        check_winner()


# Function to check if there is a winner
def check_winner():
    # Access the global variable game_over
    global game_over

    # Check rows for a win
    for i in range(3):
        if (
            buttons[i][0]["text"]
            == buttons[i][1]["text"]
            == buttons[i][2]["text"]
            != ""
        ):
            # Highlight the winning row in green
            buttons[i][0].config(bg="green")
            buttons[i][1].config(bg="green")
            buttons[i][2].config(bg="green")
            game_over = True

    # Check columns for a win
    for i in range(3):
        if (
            buttons[0][i]["text"]
            == buttons[1][i]["text"]
            == buttons[2][i]["text"]
            != ""
        ):
            # Highlight the winning column in green
            buttons[0][i].config(bg="green")
            buttons[1][i].config(bg="green")
            buttons[2][i].config(bg="green")
            game_over = True

    # Check diagonals for a win
    if buttons[0][0]["text"] == buttons[1][1]["text"] == buttons[2][2]["text"] != "":
        # Highlight the winning diagonal in green
        buttons[0][0].config(bg="green")
        buttons[1][1].config(bg="green")
        buttons[2][2].config(bg="green")
        game_over = True
    if buttons[0][2]["text"] == buttons[1][1]["text"] == buttons[2][0]["text"] != "":
        # Highlight the winning diagonal in green
        buttons[0][2].config(bg="green")
        buttons[1][1].config(bg="green")
        buttons[2][0].config(bg="green")
        game_over = True

    # Check if the game is a draw
    if (
        all(buttons[i][j]["text"] != "" for i in range(3) for j in range(3))
        and not game_over
    ):
        game_over = True
        messagebox.showinfo("Tic Tac Toe", "It's a draw!")
        reset_game()

    # If the game is over, show a message box announcing the winner and reset the game
    if game_over:
        winner = "O" if current_player == "X" else "X"
        messagebox.showinfo("Tic Tac Toe", f"Player {winner} wins!")
        reset_game()


# Function to reset the game
def reset_game():
    # Access the global variables current_player and game_over
    global current_player, game_over
    # Reset the current player to X and the game_over flag to False
    current_player = "X"
    game_over = False
    # Clear the text and background color of all buttons
    for i in range(3):
        for j in range(3):
            buttons[i][j].config(text="", bg="SystemButtonFace")


# Create the main application window
app = tk.Tk()
app.title("Tic Tac Toe")

# Initialize the current player to X and the game_over flag to False
current_player = "X"
game_over = False

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

# Place the buttons in the grid
for i in range(3):
    for j in range(3):
        buttons[i][j].grid(row=i, column=j)

# Start the main event loop
app.mainloop()
