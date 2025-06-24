import tkinter as tk

class MusicPlayerApp:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("🎶 Playlist Widget")
        self.window.geometry("600x700")

    def run(self):
        self.window.mainloop()