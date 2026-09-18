from enum import Enum

from src.vision.hand import Hand


class Direction(Enum):
    NONE = "NONE"
    LEFT = "LEFT"
    RIGHT = "RIGHT"
    UP = "UP"
    DOWN = "DOWN"


class HandDirection:
    """
    Detecta la dirección de movimiento de una mano.
    """

    def __init__(self, threshold=0.01):
        self.threshold = threshold
        self.previous_positions = {}

    def get_direction(self, hand: Hand) -> Direction:
        wrist = hand.landmarks[0]

        current_position = (
            wrist.x,
            wrist.y,
        )

        hand_id = hand.handedness

        if hand_id not in self.previous_positions:
            self.previous_positions[hand_id] = current_position
            return Direction.NONE

        previous_position = self.previous_positions[hand_id]

        dx = current_position[0] - previous_position[0]
        dy = current_position[1] - previous_position[1]

        self.previous_positions[hand_id] = current_position

        if abs(dx) < self.threshold and abs(dy) < self.threshold:
            return Direction.NONE

        if abs(dx) > abs(dy):
            if dx > 0:
                return Direction.RIGHT

            return Direction.LEFT

        if dy > 0:
            return Direction.DOWN

        return Direction.UP