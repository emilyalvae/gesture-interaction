import cv2

from src.vision.camera import Camera
from src.vision.hand_tracker import HandTracker
from src.vision.renderer import Renderer
from src.vision.hand_velocity import HandVelocity
from src.vision.hand_direction import HandDirection

from src.gestures.gesture_detector import GestureDetector
from src.gestures.movement_detector import MovementDetector
from src.gestures.dynamic_gesture_detector import DynamicGestureDetector


def main():
    camera = Camera()
    tracker = HandTracker()
    renderer = Renderer()

    gesture_detector = GestureDetector()
    velocity_detector = HandVelocity()
    movement_detector = MovementDetector()
    direction_detector = HandDirection()
    dynamic_detector = DynamicGestureDetector()

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

                # Gesto estático
                gesture = gesture_detector.detect(hand)

                # Velocidad
                velocity = velocity_detector.get_velocity(hand)

                # Tipo de movimiento
                movement = movement_detector.detect(velocity)

                # Dirección
                direction = direction_detector.get_direction(hand)

                # Gesto dinámico
                dynamic_gesture = dynamic_detector.detect(
                    gesture,
                    movement,
                    direction,
                )

                text = (
                    f"{hand.handedness}: "
                    f"G:{gesture.value} | "
                    f"V:{velocity:.3f} | "
                    f"M:{movement.value} | "
                    f"D:{direction.value} | "
                    f"DG:{dynamic_gesture.value}"
                )

                cv2.putText(
                    frame,
                    text,
                    (20, y),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.65,
                    (255, 255, 255),
                    2,
                )

                y += 35

            cv2.imshow("Dynamic Gesture Test", frame)

            if cv2.waitKey(1) == 27:
                break

    finally:
        camera.release()


if __name__ == "__main__":
    main()