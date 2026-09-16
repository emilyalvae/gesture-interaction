from src.vision.hand import Hand


class HandVelocity:
    """
    Calcula la velocidad aproximada de movimiento de cada mano.
    """

    def __init__(self):
        self.previous_positions = {}

    def get_velocity(self, hand: Hand):
        wrist = hand.landmarks[0]

        current_position = (
            wrist.x,
            wrist.y,
            wrist.z,
        )

        # Usamos la lateralidad para mantener
        # una posición independiente por cada mano.
        hand_id = hand.handedness

        if hand_id not in self.previous_positions:
            self.previous_positions[hand_id] = current_position
            return 0.0

        previous_position = self.previous_positions[hand_id]

        dx = current_position[0] - previous_position[0]
        dy = current_position[1] - previous_position[1]
        dz = current_position[2] - previous_position[2]

        velocity = (dx * dx + dy * dy + dz * dz) ** 0.5

        self.previous_positions[hand_id] = current_position

        return velocity