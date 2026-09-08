import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))

import cv2

from vision.camera import Camera
from vision.hand_tracker import HandTracker
from vision.renderer import Renderer
from gestures.gesture_detector import GestureDetector


def main():

    camera = Camera()
    tracker = HandTracker()
    renderer = Renderer()
    gesture_detector = GestureDetector()

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

                gesture = gesture_detector.detect(hand)

                cv2.putText(
                    frame,
                    f"{hand.handedness}: {gesture.value}",
                    (20, y),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.8,
                    (0, 255, 0),
                    2,
                )

                y += 40

            cv2.imshow("Gesture Test", frame)

            if cv2.waitKey(1) == 27:
                break

    finally:
        camera.release()


if __name__ == "__main__":
    main()