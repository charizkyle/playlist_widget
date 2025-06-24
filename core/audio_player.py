import pygame

class AudioPlayer:
    def __init__(self):
        self._paused = False
        self._current_position = 0

    def play(self, file_path):
        pygame.mixer.music.load(file_path)
        pygame.mixer.music.play()
        self._paused = False
        self._current_position = 0

    def pause(self):
        pygame.mixer.music.pause()
        self._paused = True

    def resume(self):
        pygame.mixer.music.unpause()
        self._paused = False

    def stop(self):
        pygame.mixer.music.stop()
        self._paused = False
        self._current_position = 0

    def get_position(self):
        return pygame.mixer.music.get_pos() / 1000  # Convert milliseconds to seconds
    
    @property
    def paused(self):
        return self._paused