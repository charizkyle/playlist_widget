import threading
import time

def start_progress_thread(audio_player, update_func):
    def update_progress():
        while True:
            if not audio_player.paused:
                update_func()
            time.sleep(0.5)
    thread = threading.Thread(target=update_progress)
    thread.daemon = True
    thread.start()