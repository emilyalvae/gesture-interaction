import time

from src.vision.hand import Hand


class HandVelocity:
    """
    Calcula la velocidad aproximada de movimiento de cada mano.
    """

    def __init__(self):
        self.previous_positions = {}
        self.previous_times = {}

    def get_velocity(self, hand: Hand):
        wrist = hand.landmarks[0]

        current_position = (
            wrist.x,
            wrist.y,
            wrist.z,
        )

        current_time = time.perf_counter()

        hand_id = hand.handedness

        if hand_id not in self.previous_positions:
            self.previous_positions[hand_id] = current_position
            self.previous_times[hand_id] = current_time
            return 0.0

        previous_position = self.previous_positions[hand_id]
        previous_time = self.previous_times[hand_id]

        delta_time = current_time - previous_time

        if delta_time <= 0:
            return 0.0

        dx = current_position[0] - previous_position[0]
        dy = current_position[1] - previous_position[1]
        dz = current_position[2] - previous_position[2]

        distance = (dx * dx + dy * dy + dz * dz) ** 0.5

        velocity = distance / delta_time

        self.previous_positions[hand_id] = current_position
        self.previous_times[hand_id] = current_time

        return velocity