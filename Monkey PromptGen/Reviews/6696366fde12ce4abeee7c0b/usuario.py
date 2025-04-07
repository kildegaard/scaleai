import time  # For simulating delays
import os

guest_rings = {}  # Dictionary to store guest ring counts


def doorbell_rung(guest_id):

    # Update or initialize the guest's ring count
    if guest_id in guest_rings:
        guest_rings[guest_id] += 1
    else:
        guest_rings[guest_id] = 1

    if guest_rings[guest_id] == 3:
        play_message(guest_id)
    print(guest_rings)


def play_message(guest_id):
    message = f"Hello, guest {guest_id}. No one is available at home right now. Please come later."
    print(message)  # Replace with actual audio playback logic
    play_custom_sound()


def play_custom_sound():
    # Path to your sound file
    file = "owner-note.wav"

    # Play sound using the appropriate command for your OS
    if os.name == "nt":  # For Windows
        os.system(f"start {file}")
    elif os.name == "posix":  # For Unix-like OS (Linux, macOS)
        if os.uname().sysname == "Darwin":  # macOS
            os.system(f"afplay {file}")
        else:  # Linux
            os.system(f"aplay {file}")


# Example usage (simulate doorbell rings)
doorbell_rung("guest1")
time.sleep(5)  # Simulate time between rings
doorbell_rung("guest2")
time.sleep(5)
doorbell_rung("guest1")
time.sleep(5)
doorbell_rung("guest1")  # Triggers the message for guest1

doorbell_rung("guest2")
time.sleep(1)  # Simulate time between rings
doorbell_rung("guest2")
time.sleep(1)
doorbell_rung("guest2")  # Triggers the message for guest1
