from dataclasses import dataclass
from typing import List

from src.vision.landmark import Landmark


@dataclass
class Hand:
    landmarks: List[Landmark]
    handedness: str
    score: float