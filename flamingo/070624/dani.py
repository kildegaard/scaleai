import cv2
import mediapipe as mp
import pyautogui
import webbrowser
import os

mp_hands = mp.solutions.hands
hands = mp_hands.Hands(min_detection_confidence=0.5, min_tracking_confidence=0.5)

cap = cv2.VideoCapture(1)

while cap.isOpened():
    success, image = cap.read()
    if not success:
        print("Ignoring empty camera frame.")
        continue

    image = cv2.cvtColor(cv2.flip(image, 1), cv2.COLOR_BGR2RGB)
    results = hands.process(image)

    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

    if results.multi_hand_landmarks:
        hand_count = len(results.multi_hand_landmarks)

        if hand_count == 2:
            pyautogui.screenshot().save("screenshot.png")
            print("Screenshot saved")

        elif hand_count == 1:
            for hand in results.multi_hand_landmarks:
                x = [landmark.x for landmark in hand.landmark]
                if x[5] < x[17]:  # Right hand
                    webbrowser.open("http://www.google.com")
                    print("Opening browser")
                else:  # Left hand
                    path = os.path.join(
                        os.path.join(os.environ["USERPROFILE"]), "Downloads"
                    )
                    os.startfile(path)
                    print("Opening downloads directory")

    cv2.imshow("MediaPipe Hands", image)
    if cv2.waitKey(5) & 0xFF == 27:
        break

hands.close()
cap.release()
