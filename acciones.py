import pyautogui
import os
import webbrowser

# Tamaño de la pantalla
ancho_pantalla, alto_pantalla = pyautogui.size()

def mover_mouse(x, y, ancho_frame, alto_frame):
    """Mueve el mouse en función de coordenadas del índice"""
    x_mouse = int(x * ancho_pantalla / ancho_frame)
    y_mouse = int(y * alto_pantalla / alto_frame)
    pyautogui.moveTo(x_mouse, y_mouse, duration=0.05)

def click_mouse():
    """Hace clic en la posición actual"""
    pyautogui.click()

def abrir_bloc_notas():
    """Abrir Bloc de Notas en Windows"""
    os.system("notepad")

def abrir_navegador():
    """Abrir navegador en Google"""
    webbrowser.open("https://www.google.com")
