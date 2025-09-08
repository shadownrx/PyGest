import cv2
from detector_manos import DetectorManos
from utils import calcular_fps, mostrar_texto
from acciones import mover_mouse, click_mouse, abrir_bloc_notas, abrir_navegador

detector = DetectorManos()
cap = cv2.VideoCapture(0)

try:
    while True:
        ret, frame = cap.read()
        if not ret:
            break

        frame = cv2.flip(frame, 1)  # Espejo
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        resultados = detector.procesar(frame_rgb)
        texto_gesto = ""

        if resultados.multi_hand_landmarks:
            for hand_landmarks in resultados.multi_hand_landmarks:
                dedos = detector.dedos_arriba(hand_landmarks)

                # Coordenadas del índice (landmark 8)
                x_indice = hand_landmarks.landmark[8].x * frame.shape[1]
                y_indice = hand_landmarks.landmark[8].y * frame.shape[0]

                # 1️⃣ Mover mouse con solo índice
                if dedos[1] == 1 and sum(dedos) == 1:
                    mover_mouse(x_indice, y_indice, frame.shape[1], frame.shape[0])
                    texto_gesto = "Mover mouse"

                # 2️⃣ Clic con índice + pulgar
                elif dedos[0] == 1 and dedos[1] == 1 and sum(dedos) == 2:
                    click_mouse()
                    texto_gesto = "Clic"

                # 3️⃣ Palma abierta (todos los dedos arriba) → Bloc de notas
                elif sum(dedos) == 5:
                    abrir_bloc_notas()
                    texto_gesto = "Abrir Bloc de notas"

                # 4️⃣ Like (solo pulgar arriba) → Navegador
                elif dedos[0] == 1 and sum(dedos) == 1:
                    abrir_navegador()
                    texto_gesto = "Abrir navegador"

        # --- Mostrar FPS y gesto detectado ---
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
