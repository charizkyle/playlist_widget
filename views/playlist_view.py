import tkinter as tk
from tkinter import filedialog
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

        self.setup_ui()
        start_progress_thread(self.audio, self.update_progress)

    def setup_ui(self):
        self.bg_image = tk.PhotoImage(file="assets/background.png")
        self.bg_label = tk.Label(self.frame, image=self.bg_image)
        self.bg_label.place(x=0, y=0, relwidth=1, relheight=1)

        self.song_title = tk.Label(self.frame, text="No song playing", font=("Arial", 16, "bold"), bg="#ffffff")
        self.song_title.place(relx=0.5, y=40, anchor="n")

        self.btn_select_folder = ctk.CTkButton(self.frame, text="🎵 Select Folder", command=self.select_music_folder)
        self.btn_select_folder.place(relx=0.5, rely=0.15, anchor="n")

        self.song_listbox = tk.Listbox(self.frame, width=50, font=("Arial", 14))
        self.song_listbox.place(relx=0.5, rely=0.25, anchor="n")

        self.pbar = Progressbar(self.frame, length=400, mode="determinate")
        self.pbar.place(relx=0.5, rely=0.68, anchor="n")

        control_frame = tk.Frame(self.frame, bg="#ffffff")
        control_frame.place(relx=0.5, rely=0.75, anchor="n")

        ctk.CTkButton(control_frame, text="⏮", command=self.prev_song, width=50).grid(row=0, column=0, padx=5)
        ctk.CTkButton(control_frame, text="▶️", command=self.play_music, width=50).grid(row=0, column=1, padx=5)
        ctk.CTkButton(control_frame, text="⏸", command=self.pause_music, width=50).grid(row=0, column=2, padx=5)
        ctk.CTkButton(control_frame, text="⏭", command=self.next_song, width=50).grid(row=0, column=3, padx=5)

    def show(self):
        self.frame.pack(fill="both", expand=True)

    def select_music_folder(self):
        path = filedialog.askdirectory()
        if path:
            self.songs.clear()
            self.song_listbox.delete(0, tk.END)
            for file in os.listdir(path):
                if file.endswith(".mp3"):
                    self.songs.append(os.path.join(path, file))
                    self.song_listbox.insert(tk.END, file)

    def play_music(self):
        if self.audio.paused:
            self.audio.resume()
        else:
            self.play_selected_song()

    def pause_music(self):
        self.audio.pause()

    def play_selected_song(self):
        if not self.song_listbox.curselection():
            return
        self.current_index = self.song_listbox.curselection()[0]
        song_path = self.songs[self.current_index]
        self.audio.play(song_path)
        self.song_title.config(text=f"Now Playing: {os.path.basename(song_path)}")

        audio = MP3(song_path)
        self.pbar["maximum"] = audio.info.length

    def next_song(self):
        if self.current_index < len(self.songs) - 1:
            self.current_index += 1
            self.song_listbox.select_clear(0, tk.END)
            self.song_listbox.select_set(self.current_index)
            self.play_selected_song()

    def prev_song(self):
        if self.current_index > 0:
            self.current_index -= 1
            self.song_listbox.select_clear(0, tk.END)
            self.song_listbox.select_set(self.current_index)
            self.play_selected_song()

    def update_progress(self):
        self.pbar["value"] = self.audio.get_position()