import tkinter as tk
from views.playlist_view import PlaylistApp

class MusicPlayerApp:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("🎶 Playlist Widget Music Player")
        width = 450
        height = 450
        self.window.geometry(f"{width}x{height}")
        self.window.resizable(False, False)
        screen_width = self.window.winfo_screenwidth()
        screen_height = self.window.winfo_screenheight()
        position_x = (screen_width // 2) - (width // 2)
        position_y = (screen_height // 2) - (height // 2)
        self.window.geometry(f"{width}x{height}+{position_x}+{position_y}")

        self.view = PlaylistApp(self.window)
        self.view.show()

    def run(self):
        self.window.mainloop()