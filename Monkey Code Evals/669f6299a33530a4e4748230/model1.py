import time
import keyboard

RECORDING_KEY = "f6"  # Customize the key to start/stop recording
PLAYBACK_DELAY = 5  # Customize the playback delay

while True:
    # Wait until the recording key is pressed
    keyboard.wait(RECORDING_KEY)
    print("Recording")

    # Record events until the recording key is pressed again
    recorded = keyboard.record(until=RECORDING_KEY)
    print("Stopped recording")

    print("Waiting")
    # Wait the given delay
    time.sleep(PLAYBACK_DELAY)
    print("Playing")

    # Replay the key presses
    keyboard.play(recorded)
    print("Finished")
