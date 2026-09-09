from enum import Enum

from src.vision.hand import Hand
from src.gestures.finger_detector import FingerDetector


class Gesture(Enum):
    OPEN_HAND = "OPEN_HAND"
    FIST = "FIST"
    POINT = "POINT"
    PINCH = "PINCH"
    UNKNOWN = "UNKNOWN"


class GestureDetector:
    """
    Detecta gestos básicos a partir del estado de los dedos
    y de la posición de los landmarks.
    """

    def __init__(self, pinch_threshold=0.06):
        self.finger_detector = FingerDetector()
        self.pinch_threshold = pinch_threshold

    def detect(self, hand: Hand) -> Gesture:

        fingers = self.finger_detector.detect(hand)

        landmarks = hand.landmarks

        # Pinch: pulgar e índice están muy cerca
        pinch_distance = self._distance(
            landmarks[4],
            landmarks[8],
        )

        if pinch_distance < self.pinch_threshold:
            return Gesture.PINCH

        # Mano abierta
        if (
            fingers.thumb
            and fingers.index
            and fingers.middle
            and fingers.ring
            and fingers.pinky
        ):
            return Gesture.OPEN_HAND

        # Puño
        if (
            not fingers.thumb
            and not fingers.index
            and not fingers.middle
            and not fingers.ring
            and not fingers.pinky
        ):
            return Gesture.FIST

        # Señalar con el índice
        if (
            fingers.index
            and not fingers.middle
            and not fingers.ring
            and not fingers.pinky
        ):
            return Gesture.POINT

        return Gesture.UNKNOWN

    def _distance(self, a, b):
        """
        Calcula la distancia euclidiana entre dos landmarks.
        """

        dx = a.x - b.x
        dy = a.y - b.y
        dz = a.z - b.z

        return (dx * dx + dy * dy + dz * dz) ** 0.5