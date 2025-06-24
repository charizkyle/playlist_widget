import tkinter as tk
import customtkinter as ctk
import pygame
import os
from core.audio_player import AudioPlayer

class PlaylistApp:
    def __init__(self, master):
        self.master = master
        self.frame = tk.Frame(master)
        self.audio = AudioPlayer()
        self.songs = []
        self.current_index = 0
        