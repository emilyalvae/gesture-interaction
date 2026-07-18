import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))

import cv2

from vision.camera import Camera
from vision.hand_tracker import HandTracker


trajectory = []


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

            if hands:

                index = hands[0].landmarks[8]

                x = int(index.x * w)
                y = int(index.y * h)

                trajectory.append((x, y))

                if len(trajectory) > 150:
                    trajectory.pop(0)

            for point in trajectory:

                cv2.circle(frame, point, 2, (0, 255, 255), -1)

            cv2.imshow("Trajectory", frame)

            if cv2.waitKey(1) == 27:
                break

    finally:
        camera.release()


if __name__ == "__main__":
    main()