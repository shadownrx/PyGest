import time
import json

# Leer configuración de gestos
with open("gestos_config.json", "r") as f:
    config = json.load(f)

# Variables globales
ultimo_tiempo = {}

def detectar_gesto(hand_landmarks, frame_shape, detector):
    """
    Detecta el gesto actual según landmarks y retorna la acción y datos.
    """
    dedos = detector.dedos_arriba(hand_landmarks)

    # Coordenadas índice y pulgar
    x_indice = int(hand_landmarks.landmark[8].x * frame_shape[1])
    y_indice = int(hand_landmarks.landmark[8].y * frame_shape[0])
    x_pulgar = int(hand_landmarks.landmark[4].x * frame_shape[1])
    y_pulgar = int(hand_landmarks.landmark[4].y * frame_shape[0])

    # Determinar gesto
    gesto = None
    # Palma abierta
    if sum(dedos) == 5:
        gesto = "palma_abierta"
    # Like (solo pulgar arriba)
    elif dedos[0] == 1 and sum(dedos) == 1:
        gesto = "like"
    # Mano derecha (para presentaciones)
    elif dedos[1] == 1 and sum(dedos) == 1:
        gesto = "mano_derecha"
    # Mano izquierda
    elif dedos[2] == 1 and sum(dedos) == 1:
        gesto = "mano_izquierda"
    # Índice solo → mover mouse
    elif dedos[1] == 1 and sum(dedos) == 1:
        gesto = "indice_solamente"
    # Pinch → clic
    distancia = ((x_indice - x_pulgar)**2 + (y_indice - y_pulgar)**2)**0.5
    if distancia < 30:
        gesto = "pinch"

    # Cooldown
    accion = None
    datos = None
    if gesto and gesto in config["gestos"]:
        accion_info = config["gestos"][gesto]
        accion = accion_info["accion"]
        datos = accion_info.get("programa") or accion_info.get("direccion")
        # Cooldown
        cd = config.get("cooldowns", {}).get(accion, 0.5)
        tiempo_actual = time.time()
        if ultimo_tiempo.get(accion, 0) + cd > tiempo_actual:
            return None, None
        ultimo_tiempo[accion] = tiempo_actual

    return accion, datos, (x_indice, y_indice, frame_shape[1], frame_shape[0])
