import pygame
import time

class AudioPlayer:
    def __init__(self):
        self._paused = False
        self._current_position = 0
        self._start_time = 0
        self._pause_time = 0
        self._playing = False

    def play(self, file_path):
        pygame.mixer.music.load(file_path)
        pygame.mixer.music.play()
        self._paused = False
        self._start_time = time.time()
        self._playing = True

    def pause(self):
        pygame.mixer.music.pause()
        self._paused = True
        self._pause_time = time.time()

    def resume(self):
        pygame.mixer.music.unpause()
        self._paused = False
        self._start_time += time.time() - self._pause_time

    def stop(self):
        pygame.mixer.music.stop()
        self._paused = False
        self._playing = False
        self._start_time = 0

    def get_position(self):
        if self._playing:
            if self._paused:
                return self._pause_time - self._start_time
            return time.time() - self._start_time
        return 0

    @property
    def paused(self):
        return self._paused