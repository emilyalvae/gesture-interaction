import cv2


class Camera:
    """Gestiona la captura de video desde la webcam."""

    def __init__(self, camera_index: int = 0):
        self.camera_index = camera_index
        self.cap = None

    def open(self):
        self.cap = cv2.VideoCapture(self.camera_index)

        if not self.cap.isOpened():
            raise RuntimeError("No se pudo abrir la cámara.")

    def read(self):
        success, frame = self.cap.read()

        if not success:
            return None

        return frame

    def release(self):
        if self.cap:
            self.cap.release()

        cv2.destroyAllWindows()