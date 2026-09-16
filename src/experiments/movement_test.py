import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))

import cv2

from vision.camera import Camera
from vision.hand_tracker import HandTracker
from vision.renderer import Renderer
from vision.hand_velocity import HandVelocity
from gestures.movement_detector import MovementDetector


def main():
    camera = Camera()
    tracker = HandTracker()
    renderer = Renderer()
    velocity = HandVelocity()
    movement_detector = MovementDetector()

    camera.open()

    try:
        while True:
            frame = camera.read()

            if frame is None:
                break

            frame = cv2.flip(frame, 1)

            hands = tracker.process(frame)

            renderer.draw_hands(frame, hands)

            y = 40

            for hand in hands:
                current_velocity = velocity.get_velocity(hand)

                movement = movement_detector.detect(
                    current_velocity
                )

                text = (
                    f"{hand.handedness}: "
                    f"{movement.value} "
                    f"({current_velocity:.3f})"
                )

                cv2.putText(
                    frame,
                    text,
                    (20, y),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.7,
                    (255, 255, 255),
                    2,
                )

                y += 35

            cv2.imshow("Movement Test", frame)

            if cv2.waitKey(1) == 27:
                break

    finally:
        camera.release()


if __name__ == "__main__":
    main()