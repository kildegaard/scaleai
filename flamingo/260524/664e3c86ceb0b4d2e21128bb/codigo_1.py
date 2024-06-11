import tkinter as tk
import random


class Cup:
    def __init__(self, canvas, x, y, colors):
        self.canvas = canvas
        self.colors = colors
        self.current_color = random.choice(colors)
        self.x = -x  # Introduce a negative value
        self.y = y
        self.size = 50
        self.canvas_id = self.draw()

    def draw(self):
        return self.canvas.create_rectangle(
            self.x,
            self.y,
            self.x + self.size,
            self.y + self.size,
            fill=self.current_color,
        )

    def fill(self, color):
        self.current_color = color
        self.canvas.itemconfig(self.canvas_id, fill=color)


class GameApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Color Mixing Game")

        self.canvas = tk.Canvas(root, width=300, height=300)
        self.canvas.pack()

        self.cups = [
            Cup(self.canvas, 50, 50, ["yellow", "red"]),
            Cup(self.canvas, 150, 50, ["red", "green"]),
            Cup(self.canvas, 50, 150, ["green", "blue"]),
            Cup(self.canvas, 150, 150, ["blue", "yellow"]),
        ]

        self.empty_cup = Cup(self.canvas, 250, 250, ["white"])

        self.canvas.bind("<Button-1>", self.click_event)

    def click_event(self, event):
        clicked_cup = None
        for cup in self.cups + [self.empty_cup]:
            x1, y1, x2, y2 = self.canvas.coords(cup.canvas_id)
            if x1 < event.x < x2 and y1 < event.y < y2:
                clicked_cup = cup
                break

        if clicked_cup:
            self.mix_colors(clicked_cup)

    def mix_colors(self, cup):
        for other_cup in self.cups + [self.empty_cup]:
            if other_cup != cup:
                other_cup.fill(cup.current_color)
        if all(cup.current_color == self.cups[0].current_color for cup in self.cups):
            self.canvas.create_text(150, 150, text="You Win!", font=("Helvetica", 24))
            self.canvas.create_text(
                150, 250, text=str(cup.current_color), font=("Helvetica", 24)
            )


if __name__ == "__main__":
    root = tk.Tk()
    app = GameApp(root)
    root.mainloop()
