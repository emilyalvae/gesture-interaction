import math

from src.vision.hand import Hand


class HandOrientation:
    """
    Calcula la orientación aproximada de la palma de la mano.
    """

    def get_orientation(self, hand: Hand):

        wrist = hand.landmarks[0]
        index_base = hand.landmarks[5]
        pinky_base = hand.landmarks[17]

        # Vector desde la base del meñique
        # hacia la base del índice.
        palm_vector = (
            index_base.x - pinky_base.x,
            index_base.y - pinky_base.y,
        )

        # Ángulo de la palma.
        angle = math.degrees(
            math.atan2(
                palm_vector[1],
                palm_vector[0],
            )
        )

        return angle