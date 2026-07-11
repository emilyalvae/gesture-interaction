import cv2

from vision.camera import Camera


def main():

    camera = Camera()

    try:

        camera.open()

        while True:

            frame = camera.read()

            if frame is None:
                break
            # Efecto espejo
            frame = cv2.flip(frame, 1)

            cv2.imshow("Gesture3D", frame)

            if cv2.waitKey(1) == 27:
                break

    finally:
        camera.release()


if __name__ == "__main__":
    main()