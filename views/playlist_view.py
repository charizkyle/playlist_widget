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
        self.song_title.place(relx=0, rely=40, anchor="n")

        self.btn_select_folder = ctk.CTkButton(self.frame, text="Select Folder", command=self.select_music_folder)
        self.btn_select_folder.place(relx=0.5, rely=0.15, anchor="n")

        self.song_listbox.place = tk.Listbox(self.frame, width=50, font=("Arial", 12))
        self.song_listbox.place(relx=0.5, rely=0.25, anchor="n")

        self.pbar = Progressbar(self.frame, length=400, mode="determinate")
        self.pbar.place(relx=0.5, rely=0.68, anchor="n")

        control_frame = tk.Frame(self.frame, bg="white")

        ctk.CTkButton(control_frame, text="⏮", command=self.prev_song, width=50).grid(row=0, column=0, padx=5)
        ctk.CTkButton(control_frame, text="▶️", command=self.play_music, width=50).grid(row=0, column=1, padx=5)