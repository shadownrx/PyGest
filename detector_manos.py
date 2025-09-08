import mediapipe as mp

mp_manos = mp.solutions.hands
mp_dibujo = mp.solutions.drawing_utils

class DetectorManos:
    def __init__(self, max_hands=2, detection_conf=0.7):
        self.manos = mp_manos.Hands(max_num_hands=max_hands, 
                                    min_detection_confidence=detection_conf)

    def dedos_arriba(self, hand_landmarks):
        """Devuelve lista [Pulgar, Índice, Medio, Anular, Meñique]"""
        dedos = []
        tips = [4, 8, 12, 16, 20]

        # Pulgar
        if hand_landmarks.landmark[tips[0]].x < hand_landmarks.landmark[tips[0]-1].x:
            dedos.append(1)
        else:
            dedos.append(0)

        # Otros dedos
        for id in range(1, 5):
            if hand_landmarks.landmark[tips[id]].y < hand_landmarks.landmark[tips[id]-2].y:
                dedos.append(1)
            else:
                dedos.append(0)

        return dedos

    def procesar(self, frame_rgb):
        """Procesa la imagen y devuelve resultados"""
        return self.manos.process(frame_rgb)
