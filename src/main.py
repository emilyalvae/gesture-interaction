import cv2

from vision.camera import Camera
from vision.hand_tracker import HandTracker
from vision.renderer import Renderer


def main():

    camera = Camera()
    tracker = HandTracker()
    renderer = Renderer()

    try:

        camera.open()

        while True:

            frame = camera.read()

            if frame is None:
                break

            # Efecto espejo
            frame = cv2.flip(frame, 1)

            # Detectar manos
            hands = tracker.process(frame)

            # Dibujar manos
            renderer.draw_hands(frame, hands)

            cv2.imshow("Gesture3D", frame)

            if cv2.waitKey(1) == 27:  # ESC
                break

    finally:
        camera.release()


if __name__ == "__main__":
    main()