from enum import Enum

from src.vision.hand import Hand
from src.gestures.finger_detector import FingerDetector


class Gesture(Enum):
    OPEN_HAND = "OPEN_HAND"
    FIST = "FIST"
    POINT = "POINT"
    UNKNOWN = "UNKNOWN"


class GestureDetector:
    """
    Detecta gestos básicos a partir del estado de los dedos.
    """

    def __init__(self):
        self.finger_detector = FingerDetector()

    def detect(self, hand: Hand) -> Gesture:

        fingers = self.finger_detector.detect(hand)

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