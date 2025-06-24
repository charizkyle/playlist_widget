import threading
import time

def start_progress_thread(update_func, audio_player):
    def update_progress():
        while True:
            if not audio_player.paused:
                update_func()
            time.sleep(0.1)

    progress_thread = threading.Thread(target=update_progress, daemon=True)
    progress_thread.start()