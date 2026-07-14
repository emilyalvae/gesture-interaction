import mediapipe as mp


class Renderer:

    def __init__(self):

        self.mp_hands = mp.solutions.hands
        self.mp_drawing = mp.solutions.drawing_utils

    def draw_hands(self, frame, results):

        if results.multi_hand_landmarks:

            for hand_landmarks in results.multi_hand_landmarks:

                self.mp_drawing.draw_landmarks(
                    frame,
                    hand_landmarks,
                    self.mp_hands.HAND_CONNECTIONS,
                )

        return frame