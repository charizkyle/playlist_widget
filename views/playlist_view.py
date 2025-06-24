import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
from tkinter.ttk import Progressbar
import customtkinter as ctk
from mutagen.mp3 import MP3
import pygame
import os
from core.audio_player import AudioPlayer
from core.utils import start_progress_thread

pygame.mixer.init()

class PlaylistApp:
    def __init__(self, master):
        self.master = master
        self.frame = tk.Frame(master)
        self.audio = AudioPlayer()
        self.songs = []
        self.current_index = 0
        self.current_song_path = ""

        self.setup_ui()
        start_progress_thread(self.audio, self.update_progress)

    def setup_ui(self):
    # Load and resize the image using PIL to fit 450x450
        bg_image = Image.open("assets/bg.png")
        resized_image = bg_image.resize((450, 450))
        self.bg_image = ImageTk.PhotoImage(resized_image)
        self.bg_label = tk.Label(self.frame, image=self.bg_image, width=450, height=450)
        self.bg_label.place(x=0, y=0, width=450, height=450)

        # Now Playing Label (top bar area)
        self.song_title = tk.Label(self.frame, text="Now Playing:", font=("Consolas", 11, "bold"), bg="#f4aaff", fg="#995edd", anchor="center", padx=10, width=30)
        self.song_title.place(x=90, y=100)

        # Progress bar (just below the display area)
        self.pbar = Progressbar(self.frame, length=350, mode="determinate")
        self.pbar["value"] = 0
        self.pbar.place(x=50, y=300)

        # Audio Controls (centered along pink wave area)
        self.btn_prev = ctk.CTkButton(self.frame, text="⏮", command=self.prev_song, width=40, fg_color="#f0758a", hover_color = "#7834c4")
        self.btn_prev.place(x=110, y=330)

        self.btn_play = ctk.CTkButton(self.frame, text="▶️", command=self.play_music, width=40, fg_color="#f0758a", hover_color = "#7834c4")
        self.btn_play.place(x=170, y=330)

        self.btn_pause = ctk.CTkButton(self.frame, text="⏸", command=self.pause_music, width=40, fg_color="#f0758a", hover_color = "#7834c4")
        self.btn_pause.place(x=230, y=330)

        self.btn_next = ctk.CTkButton(self.frame, text="⏭", command=self.next_song, width=40, fg_color="#f0758a", hover_color = "#7834c4")
        self.btn_next.place(x=290, y=330)

        # Folder Button (at bottom pink box area)
        self.btn_select_folder = ctk.CTkButton(
        self.frame, text="🎵 Select Music Folder", command=self.select_music_folder, width=200, font=("Consolas", 12, "bold"), fg_color = "#f0758a", hover_color = "#7834c4")
        self.btn_select_folder.place(x=120, y=370)

    def show(self):
        self.frame.pack(fill="both", expand=True)

    def select_music_folder(self):
        path = filedialog.askdirectory()
        if path:
            self.songs.clear()
            for file in os.listdir(path):
                if file.endswith(".mp3"):
                    self.songs.append(os.path.join(path, file))
            if self.songs:
                self.current_index = 0
                self.play_selected_song()

    def play_music(self):
        if self.audio.paused:
            self.audio.resume()
        else:
            self.play_selected_song()

    def pause_music(self):
        self.audio.pause()

    def play_selected_song(self):
        if not self.songs:
            return
        song_path = self.songs[self.current_index]
        self.current_song_path = song_path
        self.audio.play(song_path)
        self.song_title.config(text=f"Now Playing: {os.path.basename(song_path)}")

        try:
            audio = MP3(song_path)
            self.pbar["maximum"] = audio.info.length
            self.pbar["value"] = 0
        except Exception as e:
            print(f"Error loading song metadata: {e}")
            self.pbar["maximum"] = 100

    def next_song(self):
        if self.current_index < len(self.songs) - 1:
            self.current_index += 1
            self.play_selected_song()

    def prev_song(self):
        if self.current_index > 0:
            self.current_index -= 1
            self.play_selected_song()

    def update_progress(self):
        if self.current_song_path:
            pos = self.audio.get_position()
            self.pbar["value"] = pos
            self.frame.update_idletasks()