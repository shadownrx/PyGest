import time
import pyautogui

# Configuración de cooldown y smoothing
COOLDOWN_CLIC = 0.5
ultimo_click = 0
ultima_posicion = None
historial_posiciones = []

def suavizar_movimiento(x, y, max_historial=5):
    """
    Aplica suavizado usando un promedio de las últimas posiciones.
    """
    global historial_posiciones
    historial_posiciones.append((x, y))
    if len(historial_posiciones) > max_historial:
        historial_posiciones.pop(0)
    prom_x = sum(p[0] for p in historial_posiciones) / len(historial_posiciones)
    prom_y = sum(p[1] for p in historial_posiciones) / len(historial_posiciones)
    return int(prom_x), int(prom_y)


def detectar_gesto(hand_landmarks, frame_shape, detector):
    """
    Detecta gestos a partir de los landmarks de la mano.
    Retorna (accion, datos) donde:
        - accion: string con el tipo de gesto ("mover", "clic", "clic_derecho", "scroll", "drag", None)
        - datos: información adicional (ej: coordenadas)
    """
    global ultimo_click, ultima_posicion
    dedos = detector.dedos_arriba(hand_landmarks)

    # Coordenadas índice y pulgar
    x_indice = int(hand_landmarks.landmark[8].x * frame_shape[1])
    y_indice = int(hand_landmarks.landmark[8].y * frame_shape[0])
    x_pulgar = int(hand_landmarks.landmark[4].x * frame_shape[1])
    y_pulgar = int(hand_landmarks.landmark[4].y * frame_shape[0])

    # --- Gestos ---
    # 1️⃣ Mover mouse (solo índice levantado)
    if dedos[1] == 1 and sum(dedos) == 1:
        x_suave, y_suave = suavizar_movimiento(x_indice, y_indice)
        return "mover", (x_suave, y_suave, frame_shape[1], frame_shape[0])

    # 2️⃣ Clic izquierdo (pinch índice + pulgar)
    distancia = ((x_indice - x_pulgar) ** 2 + (y_indice - y_pulgar) ** 2) ** 0.5
    if distancia < 30:
        tiempo_actual = time.time()
        if tiempo_actual - ultimo_click > COOLDOWN_CLIC:
            ultimo_click = tiempo_actual
            return "clic", None

    # 3️⃣ Clic derecho (✌️ índice + medio arriba)
    if dedos[1] == 1 and dedos[2] == 1 and sum(dedos) == 2:
        tiempo_actual = time.time()
        if tiempo_actual - ultimo_click > COOLDOWN_CLIC:
            ultimo_click = tiempo_actual
            return "clic_derecho", None

    # 4️⃣ Scroll (índice + medio levantados moviéndose)
    if dedos[1] == 1 and dedos[2] == 1 and sum(dedos) == 2:
        if ultima_posicion:
            dy = y_indice - ultima_posicion[1]
            if abs(dy) > 20:  # movimiento vertical
                if dy < 0:
                    return "scroll", "arriba"
                else:
                    return "scroll", "abajo"
        ultima_posicion = (x_indice, y_indice)

    # 5️⃣ Drag (puño cerrado ✊)
    if sum(dedos) == 0:
        return "drag", "down"
    elif sum(dedos) == 5 and ultima_posicion:  # abre la mano
        return "drag", "up"

    return None, None
