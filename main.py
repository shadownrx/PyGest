import cv2
from detector_manos import DetectorManos
from utils import calcular_fps, mostrar_texto
from config import GESTOS

detector = DetectorManos()
cap = cv2.VideoCapture(0)

try:
    while True:
        ret, frame = cap.read()
        if not ret:
            break

        frame = cv2.flip(frame, 1)
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        resultados = detector.procesar(frame_rgb)
        texto_gesto = ""

        if resultados.multi_hand_landmarks:
            for hand_landmarks in resultados.multi_hand_landmarks:
                dedos = detector.dedos_arriba(hand_landmarks)

                # Mapeamos gestos
                if sum(dedos) == 0:
                    texto_gesto = "No"
                elif dedos[0] == 1 and sum(dedos) == 1:
                    texto_gesto = "Hola"
                elif dedos[1] == 1 and sum(dedos) == 1:
                    texto_gesto = "Sí"

                # Ejecutar acción si existe en config
                if texto_gesto in GESTOS:
                    GESTOS[texto_gesto]()

        fps = calcular_fps()
        if texto_gesto:
            mostrar_texto(frame, f"Gesto: {texto_gesto}", (50, 100))
        mostrar_texto(frame, f"FPS: {fps}", (10, 30), (255, 0, 0))

        cv2.imshow("Control por gestos", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

finally:
    cap.release()
    cv2.destroyAllWindows()
