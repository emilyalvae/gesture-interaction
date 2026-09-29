from enum import Enum

from src.gestures.gesture_detector import Gesture
from src.gestures.movement_detector import Movement
from src.vision.hand_direction import Direction


class DynamicGesture(Enum):
    NONE = "NONE"
    THROW = "THROW"


class DynamicGestureDetector:
    """
    Detecta gestos dinámicos combinando gesto,
    movimiento y dirección.
    """

    def detect(
        self,
        gesture: Gesture,
        movement: Movement,
        direction: Direction,
    ) -> DynamicGesture:

        if (
            gesture == Gesture.PINCH
            and movement == Movement.FAST
            and direction != Direction.NONE
        ):
            return DynamicGesture.THROW

        return DynamicGesture.NONE