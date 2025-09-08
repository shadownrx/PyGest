import cv2
from detector_manos import DetectorManos
from utils import calcular_fps, mostrar_texto
from gestos import detectar_gesto
from acciones import (
    mover_mouse,
    click_mouse,
    click_derecho,
    hacer_scroll,
    drag_mouse,
    abrir_bloc_notas,
    abrir_navegador,
)

# Inicializar detector y cámara
detector = DetectorManos()
cap = cv2.VideoCapture(0)


def procesar_frame(frame):
    """
    Procesa un frame: detección de manos + gestos.
    """
    frame = cv2.flip(frame, 1)  # espejo
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    resultados = detector.procesar(frame_rgb)

    texto_gesto = None
    if resultados.multi_hand_landmarks:
        for hand_landmarks in resultados.multi_hand_landmarks:
            accion, datos = detectar_gesto(hand_landmarks, frame.shape, detector)

            if accion == "mover":
                mover_mouse(*datos)
                texto_gesto = "Mover mouse"

            elif accion == "clic":
                click_mouse()
                texto_gesto = "Clic izquierdo"

            elif accion == "clic_derecho":
                click_derecho()
                texto_gesto = "Clic derecho"

            elif accion == "scroll":
                hacer_scroll(datos)
                texto_gesto = f"Scroll {datos}"

            elif accion == "drag":
                drag_mouse(datos)
                texto_gesto = f"Drag {datos}"

            elif accion == "abrir_bloc":
                abrir_bloc_notas()
                texto_gesto = "Abrir Bloc de notas"

            elif accion == "abrir_nav":
                abrir_navegador()
                texto_gesto = "Abrir navegador"

    # Mostrar FPS y gesto
    fps = calcular_fps()
    if texto_gesto:
        mostrar_texto(frame, f"Gesto: {texto_gesto}", (50, 100))
    mostrar_texto(frame, f"FPS: {fps}", (10, 30), (255, 0, 0))

    return frame


def main():
    try:
        while True:
            ret, frame = cap.read()
            if not ret:
                break

            frame = procesar_frame(frame)
            cv2.imshow("Control por gestos v1.0", frame)

            if cv2.waitKey(1) & 0xFF == ord("q"):
                break
    finally:
        cap.release()
        cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
