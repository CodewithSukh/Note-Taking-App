import tkinter as tk
from tkinter import messagebox, filedialog
import os


class NotesApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Notes App")
        self.root.geometry("400x400")

        self.note_text = tk.Text(self.root, wrap='word')
        self.note_text.pack(expand=1, fill='both')

        self.save_button = tk.Button(self.root, text="Save Note", command=self.save_note)
        self.save_button.pack(side='left')

        self.load_button = tk.Button(self.root, text="Load Note", command=self.load_note)
        self.load_button.pack(side='right')

    def save_note(self):
        note_content = self.note_text.get(1.0, tk.END).strip()
        if note_content:
            file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt"), ("all files", "*.*")])
            
            if file_path:
                with open("note.txt", "w") as file:
                    file.write(note_content)
            messagebox.showinfo("Info", "Note saved successfully!")
        else:
            messagebox.showwarning("Warning", "Note content is empty!")

    def load_note(self):
        if os.path.exists("note.txt"):
            with open("note.txt", "r") as file:
                note_content = file.read()
            self.note_text.delete(1.0, tk.END)
            self.note_text.insert(tk.END, note_content)
        else:
            messagebox.showwarning("Warning", "No saved note found!")

if __name__ == "__main__":
    root = tk.Tk()
    app = NotesApp(root)
    root.mainloop()
