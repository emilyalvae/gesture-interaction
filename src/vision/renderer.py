import cv2


class Renderer:

    CONNECTIONS = [
        (0,1),(1,2),(2,3),(3,4),
        (0,5),(5,6),(6,7),(7,8),
        (5,9),(9,10),(10,11),(11,12),
        (9,13),(13,14),(14,15),(15,16),
        (13,17),(17,18),(18,19),(19,20),
        (0,17)
    ]

    def draw_hands(self, frame, hands):

        h, w = frame.shape[:2]

        for hand in hands:

            # Dibujar puntos
            for landmark in hand.landmarks:

                x = int(landmark.x * w)
                y = int(landmark.y * h)

                cv2.circle(frame, (x, y), 5, (0,255,0), -1)

            # Dibujar conexiones
            for start, end in self.CONNECTIONS:

                p1 = hand.landmarks[start]
                p2 = hand.landmarks[end]

                x1 = int(p1.x * w)
                y1 = int(p1.y * h)

                x2 = int(p2.x * w)
                y2 = int(p2.y * h)

                cv2.line(frame, (x1,y1), (x2,y2), (255,0,0), 2)

        return frame