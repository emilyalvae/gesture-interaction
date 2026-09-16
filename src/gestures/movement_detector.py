from enum import Enum


class Movement(Enum):
    STILL = "STILL"
    SLOW = "SLOW"
    FAST = "FAST"


class MovementDetector:
    """
    Clasifica el movimiento de una mano según su velocidad.
    """

    def __init__(self, slow_threshold=0.08, fast_threshold=0.30):
        self.slow_threshold = slow_threshold
        self.fast_threshold = fast_threshold

    def detect(self, velocity: float) -> Movement:

        if velocity < self.slow_threshold:
            return Movement.STILL

        if velocity < self.fast_threshold:
            return Movement.SLOW

        return Movement.FAST