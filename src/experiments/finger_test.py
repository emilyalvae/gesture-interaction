import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))

import cv2

from vision.camera import Camera
from vision.hand_tracker import HandTracker
from gestures.finger_detector import FingerDetector


def main():

    camera = Camera()
    tracker = HandTracker()
    detector = FingerDetector()

    camera.open()

    try:

        while True:

            frame = camera.read()

            if frame is None:
                break

            frame = cv2.flip(frame, 1)

            hands = tracker.process(frame)

            y = 40

            for hand in hands:

                fingers = detector.detect(hand)

                text = (
                    f"{hand.handedness}: "
                    f"T:{int(fingers.thumb)} "
                    f"I:{int(fingers.index)} "
                    f"M:{int(fingers.middle)} "
                    f"R:{int(fingers.ring)} "
                    f"P:{int(fingers.pinky)}"
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

            cv2.imshow("Finger Test", frame)

            if cv2.waitKey(1) == 27:
                break

    finally:
        camera.release()


if __name__ == "__main__":
    main()