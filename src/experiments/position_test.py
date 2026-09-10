import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))

import cv2

from vision.camera import Camera
from vision.hand_tracker import HandTracker
from vision.renderer import Renderer
from vision.hand_position import HandPosition


def main():

    camera = Camera()
    tracker = HandTracker()
    renderer = Renderer()
    position = HandPosition()

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

                x, y_pos, z = position.get_wrist_position(hand)

                text = (
                    f"{hand.handedness}: "
                    f"X:{x:.2f} "
                    f"Y:{y_pos:.2f} "
                    f"Z:{z:.2f}"
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

            cv2.imshow("Position Test", frame)

            if cv2.waitKey(1) == 27:
                break

    finally:
        camera.release()


if __name__ == "__main__":
    main()