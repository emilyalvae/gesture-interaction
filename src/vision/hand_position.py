from src.vision.hand import Hand


class HandPosition:
    """
    Obtiene la posición de una mano utilizando sus landmarks.
    """

    def get_wrist_position(self, hand: Hand):
        wrist = hand.landmarks[0]

        return (
            wrist.x,
            wrist.y,
            wrist.z,
        )