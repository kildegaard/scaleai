import tkinter as tk
from tkinter import filedialog, messagebox
import sys


class TextEditor:
    def __init__(self, root, file_path):
        self.root = root
        self.file_path = file_path
        self.text_area = tk.Text(self.root)
        self.text_area.pack(fill=tk.BOTH, expand=1)
        self.save_button = tk.Button(self.root, text="Save", command=self.save_file)
        self.save_button.pack()
        self.load_file()

    def load_file(self):
        try:
            with open(self.file_path, "r") as file:
                self.text_area.insert(tk.INSERT, file.read())
        except FileNotFoundError:
            messagebox.showerror("Error", "File not found")

    def save_file(self):
        try:
            with open(self.file_path, "w") as file:
                file.write(self.text_area.get("1.0", tk.END))
            messagebox.showinfo("Success", "File saved successfully")
        except Exception as e:
            messagebox.showerror("Error", str(e))


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python text_editor.py <file_path>")
        sys.exit(1)

    file_path = sys.argv[1]
    root = tk.Tk()
    text_editor = TextEditor(root, file_path)
    root.mainloop()
