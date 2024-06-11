import tkinter as tk
from tkinter import filedialog, messagebox
import sys


def open_file(filename):
    try:
        with open(filename, "r") as file:
            return file.read()
    except FileNotFoundError:
        messagebox.showerror("Error", "File not found")
        return ""


def save_file(filename, text):
    try:
        with open(filename, "w") as file:
            file.write(text)
    except Exception as e:
        messagebox.showerror("Error", str(e))


def main():
    if len(sys.argv) != 2:
        print("Usage: python text_editor.py <filename>")
        return

    filename = sys.argv[1]

    root = tk.Tk()
    root.title("Text Editor")

    text_area = tk.Text(root)
    text_area.pack(fill="both", expand=True)

    text_area.insert("1.0", open_file(filename))

    def save_button_clicked():
        text = text_area.get("1.0", "end-1c")
        save_file(filename, text)

    save_button = tk.Button(root, text="Save", command=save_button_clicked)
    save_button.pack()

    root.mainloop()


if __name__ == "__main__":
    main()
