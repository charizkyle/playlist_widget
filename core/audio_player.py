import pygame

class AudioPlayer:
    def __init__(self):
        self.paused = False
        self.current_position = 0

    def play(self, file_path):
        pygame.mixer.music.load(file_path)
        pygame.mixer.music.play()
        self.paused = False
        self.current_position = 0

    def pause(self):
        pygame.mixer.music.pause()
        self.paused = True

    def resume(self):
        pygame.mixer.music.unpause()
        self.paused = False