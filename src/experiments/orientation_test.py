import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))

import cv2

from vision.camera import Camera
from vision.hand_tracker import HandTracker
from vision.renderer import Renderer
from vision.hand_orientation import HandOrientation


def main():

    camera = Camera()
    tracker = HandTracker()
    renderer = Renderer()
    orientation = HandOrientation()

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

                angle = orientation.get_orientation(hand)

                text = (
                    f"{hand.handedness}: "
                    f"Angle: {angle:.1f}°"
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

            cv2.imshow("Orientation Test", frame)

            if cv2.waitKey(1) == 27:
                break

    finally:
        camera.release()


if __name__ == "__main__":
    main()