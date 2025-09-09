import cv2
from detector_manos import DetectorManos
from utils import calcular_fps, mostrar_texto
from gestos import detectar_gesto
from acciones import (
    mover_mouse, click_mouse, click_derecho, hacer_scroll,
    drag_mouse, abrir_app, presentacion
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

            # Detectar gesto
            resultado = detectar_gesto(hand_landmarks, frame.shape, detector)
            if resultado is None:
                continue  # no hay gesto detectado
            accion, datos, coords = resultado

            # Ejecutar acción según tipo de gesto
            if accion == "mover_mouse" and coords:
                mover_mouse(*coords)
                texto_gesto = "Mover mouse"

            elif accion == "clic":
                click_mouse()
                texto_gesto = "Clic izquierdo"

            elif accion == "clic_derecho":
                click_derecho()
                texto_gesto = "Clic derecho"

            elif accion == "scroll" and datos:
                hacer_scroll(datos)
                texto_gesto = f"Scroll {datos}"

            elif accion == "drag" and datos:
                drag_mouse(datos)
                texto_gesto = f"Drag {datos}"

            elif accion == "abrir_app" and datos:
                abrir_app(datos)
                texto_gesto = f"Abrir {datos}"

            elif accion == "presentacion" and datos:
                presentacion(datos)
                texto_gesto = f"Presentación {datos}"

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
            cv2.imshow("Control por gestos v1.1", frame)

            if cv2.waitKey(1) & 0xFF == ord("q"):
                break
    finally:
        cap.release()
        cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
