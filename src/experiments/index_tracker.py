import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))

import cv2

from vision.camera import Camera
from vision.hand_tracker import HandTracker


def main():

    camera = Camera()
    tracker = HandTracker()

    camera.open()

    try:

        while True:

            frame = camera.read()

            if frame is None:
                break

            frame = cv2.flip(frame, 1)

            hands = tracker.process(frame)

            h, w = frame.shape[:2]

            for hand in hands:

                index_tip = hand.landmarks[8]

                x = int(index_tip.x * w)
                y = int(index_tip.y * h)

                cv2.circle(frame, (x, y), 20, (0, 0, 255), -1)

            cv2.imshow("Index Tracker", frame)

            if cv2.waitKey(1) == 27:
                break

    finally:
        camera.release()


if __name__ == "__main__":
    main()