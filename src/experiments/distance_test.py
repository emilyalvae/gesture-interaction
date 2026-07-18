import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))

import cv2
import math

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

                thumb = hand.landmarks[4]
                index = hand.landmarks[8]

                x1 = int(thumb.x * w)
                y1 = int(thumb.y * h)

                x2 = int(index.x * w)
                y2 = int(index.y * h)

                distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

                cv2.circle(frame, (x1, y1), 10, (255, 0, 0), -1)
                cv2.circle(frame, (x2, y2), 10, (0, 255, 0), -1)

                cv2.line(frame, (x1, y1), (x2, y2), (255, 255, 255), 2)

                cv2.putText(
                    frame,
                    f"{distance:.1f}px",
                    (30, 40),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    1,
                    (0, 255, 255),
                    2,
                )

            cv2.imshow("Distance Test", frame)

            if cv2.waitKey(1) == 27:
                break

    finally:
        camera.release()


if __name__ == "__main__":
    main()