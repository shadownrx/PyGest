import time
import json

# Leer configuración de gestos
with open("gestos_config.json", "r") as f:
    config = json.load(f)

# Variables globales
ultimo_tiempo = {}
historial_posiciones = []

def suavizar_movimiento(x, y, max_historial=5):
    """
    Suavizado del mouse usando promedio de últimas posiciones
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
    Detecta gestos y devuelve: accion, datos, coords
    coords = None si no aplica (ej: abrir app, presentación)
    """
    dedos = detector.dedos_arriba(hand_landmarks)

    # Coordenadas índice y pulgar (solo si se usan)
    x_indice = int(hand_landmarks.landmark[8].x * frame_shape[1])
    y_indice = int(hand_landmarks.landmark[8].y * frame_shape[0])
    x_pulgar = int(hand_landmarks.landmark[4].x * frame_shape[1])
    y_pulgar = int(hand_landmarks.landmark[4].y * frame_shape[0])

    gesto_detectado = None
    coords = None
    datos = None
    accion = None

    # Determinar gesto según dedos levantados
    if sum(dedos) == 5:
        gesto_detectado = "palma_abierta"
    elif dedos[0] == 1 and sum(dedos) == 1:
        gesto_detectado = "like"
    elif dedos[1] == 1 and sum(dedos) == 1:
        gesto_detectado = "mano_derecha"
    elif dedos[2] == 1 and sum(dedos) == 1:
        gesto_detectado = "mano_izquierda"
    elif dedos[1] == 1 and sum(dedos) == 1:
        gesto_detectado = "indice_solamente"
        coords = suavizar_movimiento(x_indice, y_indice, 5)
        coords = (*coords, frame_shape[1], frame_shape[0])
    # Pinch → clic izquierdo
    distancia = ((x_indice - x_pulgar)**2 + (y_indice - y_pulgar)**2)**0.5
    if distancia < 30:
        gesto_detectado = "pinch"

    if gesto_detectado and gesto_detectado in config["gestos"]:
        accion_info = config["gestos"][gesto_detectado]
        accion = accion_info["accion"]
        datos = accion_info.get("programa") or accion_info.get("direccion")

        # Cooldown
        cd = config.get("cooldowns", {}).get(accion, 0.5)
        tiempo_actual = time.time()
        if ultimo_tiempo.get(accion, 0) + cd > tiempo_actual:
            return None, None, None
        ultimo_tiempo[accion] = tiempo_actual

    return accion, datos, coords
