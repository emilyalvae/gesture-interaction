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

        print(
            f"Gesture={gesture}, "
            f"Movement={movement}, "
            f"Direction={direction}"
        )

        if gesture == Gesture.PINCH:
            print("PINCH OK")

        if movement == Movement.FAST:
            print("FAST OK")

        if direction != Direction.NONE:
            print("DIRECTION OK")

        if (
            gesture == Gesture.PINCH
            and movement == Movement.FAST
            and direction != Direction.NONE
        ):
            print(">>> THROW DETECTED <<<")
            return DynamicGesture.THROW

        return DynamicGesture.NONE