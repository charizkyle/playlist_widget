import tkinter as tk
from tkinter import filedialog
from tkinter.ttk import Progressbar
import customtkinter as ctk
from mutagen.mp3 import MP3
import pygame
import os
from core.audio_player import AudioPlayer
from core.utils import start_progress_thread

class PlaylistApp:
    def __init__(self, master):
        self.master = master
        self.frame = tk.Frame(master)
        self.audio = AudioPlayer()
        self.songs = []
        self.current_index = 0

        self.setup_ui()
        start_progress_thread(self.update_progress, self.audio)

    def setup_ui(self):
        self.bg_image = tk.PhotoImage(file="assets/background.png")
        self.bg_label = tk.Label(self.frame, image=self.bg_image)
        self.bg_label.place(x=0, y=0, relwidth=1, relheight=1)

        self.song_title = tk.Label(self.frame, text="No song playing", font=("Arial", 16, "bold"), bg="white")