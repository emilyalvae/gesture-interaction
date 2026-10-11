
from collections import deque

from src.vision.hand import Hand


class HandTrajectory:
    """
    Almacena la trayectoria de la punta del dedo índice
    de cada mano detectada.
    """

    def __init__(self, max_points=150):
        self.max_points = max_points
        self.trajectories = {}

    def update(self, hand: Hand):
        hand_id = hand.handedness
        index_tip = hand.landmarks[8]

        position = (
            index_tip.x,
            index_tip.y,
            index_tip.z,
        )

        if hand_id not in self.trajectories:
            self.trajectories[hand_id] = deque(
                maxlen=self.max_points
            )

        self.trajectories[hand_id].append(position)

        return list(self.trajectories[hand_id])

    def get_trajectory(self, hand_id):
        trajectory = self.trajectories.get(hand_id, ())
        return list(trajectory)

    def reset(self, hand_id=None):
        if hand_id is None:
            self.trajectories.clear()
        else:
            self.trajectories.pop(hand_id, None)
 