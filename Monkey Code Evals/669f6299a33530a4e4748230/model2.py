import time
import keyboard

# Configuration
RECORDING_KEY = "r"  # Key to start/stop recording
PLAYBACK_KEY = "p"  # Key to trigger playback
PLAYBACK_DELAY = 5  # Delay (in seconds) before playback starts

# Initialize variables
recording = False
events = []  # Store recorded key events (key, time)


def record_key(event):
    """Records key events while recording is active."""
    global recording, events
    if recording:
        events.append((event.name, time.time()))


def playback():
    """Plays back recorded key events."""
    if events:
        start_time = time.time() + PLAYBACK_DELAY
        print(f"Playback starting in {PLAYBACK_DELAY} seconds...")

        for key, timestamp in events:
            delay = timestamp - start_time
            if delay > 0:
                time.sleep(delay)
            keyboard.press_and_release(key)


# Bind keyboard events
keyboard.on_press(record_key)

# Main loop
while True:
    if keyboard.is_pressed(RECORDING_KEY):
        recording = not recording
        if recording:
            print("Recording started")
        else:
            print("Recording stopped")

    if keyboard.is_pressed(PLAYBACK_KEY):
        playback()
