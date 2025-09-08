import cv2
import time

prev_time = 0

def calcular_fps():
    global prev_time
    curr_time = time.time()
    fps = 1 / (curr_time - prev_time) if prev_time != 0 else 0
    prev_time = curr_time
    return int(fps)

def mostrar_texto(frame, texto, posicion=(50, 100), color=(0, 255, 0)):
    cv2.putText(frame, texto, posicion,
                cv2.FONT_HERSHEY_SIMPLEX, 2, color, 3)
