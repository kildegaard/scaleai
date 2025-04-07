import time  # For simulating delays

guest_rings = {}  # Dictionary to store guest ring counts
total_rings = 0  # Total ring counter


def doorbell_rung(guest_id):
    global total_rings

    total_rings += 1

    # Update or initialize the guest's ring count
    if guest_id in guest_rings:
        guest_rings[guest_id] += 1
    else:
        guest_rings[guest_id] = 1

    if total_rings >= 3 and guest_rings[guest_id] == 2:
        play_message(guest_id)


def play_message(guest_id):
    message = f"Hello, guest {guest_id}. No one is available at home right now. Please come later."
    print(message)  # Replace with actual audio playback logic


# Example usage (simulate doorbell rings)
doorbell_rung("guest1")
time.sleep(1)  # Simulate time between rings
doorbell_rung("guest2")
time.sleep(1)
doorbell_rung("guest1")  # Triggers the message for guest1
