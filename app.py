import tkinter as tk
from views.playlist_view import PlaylistApp

class MusicPlayerApp:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("🎶 Music Player")
        self.window.geometry("600x700")

        self.view = PlaylistApp(self.window)
        self.view.show()

    def run(self):
        self.window.mainloop()