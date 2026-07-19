import cv2
import mediapipe as mp

from src.vision.hand import Hand
from src.vision.landmark import Landmark


class HandTracker:
    """
    Detecta manos utilizando MediaPipe.
    """

    def __init__(
        self,
        max_num_hands=2,
        min_detection_confidence=0.7,
        min_tracking_confidence=0.7,
    ):

        self.mp_hands = mp.solutions.hands

        self.hands = self.mp_hands.Hands(
            static_image_mode=False,
            max_num_hands=max_num_hands,
            min_detection_confidence=min_detection_confidence,
            min_tracking_confidence=min_tracking_confidence,
        )

    def process(self, frame):

        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        results = self.hands.process(rgb_frame)

        hands = []

        if results.multi_hand_landmarks:

            for hand_landmarks, handedness in zip(
                results.multi_hand_landmarks,
                results.multi_handedness,
            ):

                landmarks = []

                for lm in hand_landmarks.landmark:

                    landmarks.append(
                        Landmark(
                            x=lm.x,
                            y=lm.y,
                            z=lm.z,
                        )
                    )

                hands.append(
                    Hand(
                        landmarks=landmarks,
                        handedness=handedness.classification[0].label,
                        score=handedness.classification[0].score,
                    )
                )

        return hands