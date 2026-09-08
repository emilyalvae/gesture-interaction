from dataclasses import dataclass

from src.vision.hand import Hand


@dataclass
class FingerState:
    thumb: bool
    index: bool
    middle: bool
    ring: bool
    pinky: bool


class FingerDetector:
    """
    Detecta qué dedos están extendidos en una mano.
    """

    def detect(self, hand: Hand) -> FingerState:
        landmarks = hand.landmarks

        return FingerState(
            thumb=self._is_thumb_open(landmarks),
            index=self._is_finger_open(landmarks, 8, 6),
            middle=self._is_finger_open(landmarks, 12, 10),
            ring=self._is_finger_open(landmarks, 16, 14),
            pinky=self._is_finger_open(landmarks, 20, 18),
        )

    def _is_finger_open(self, landmarks, tip_index, pip_index):
        """
        Para los cuatro dedos principales:
        si la punta está por encima de la articulación PIP,
        consideramos el dedo extendido.
        """

        tip = landmarks[tip_index]
        pip = landmarks[pip_index]

        return tip.y < pip.y

    def _is_thumb_open(self, landmarks):
        """
        Detección inicial del pulgar utilizando su posición horizontal.
        """

        tip = landmarks[4]
        ip = landmarks[3]

        return abs(tip.x - ip.x) > 0.04