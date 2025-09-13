import pyautogui
import os

def mover_mouse(x, y, ancho, alto):
    screen_w, screen_h = pyautogui.size()
    new_x = int(x / ancho * screen_w)
    new_y = int(y / alto * screen_h)
    pyautogui.moveTo(new_x, new_y)

def click_mouse():
    pyautogui.click()

def click_derecho():
    pyautogui.rightClick()

def hacer_scroll(direccion):
    if direccion == "arriba":
        pyautogui.scroll(100)
    elif direccion == "abajo":
        pyautogui.scroll(-100)

def drag_mouse(accion):
    if accion == "down":
        pyautogui.mouseDown()
    elif accion == "up":
        pyautogui.mouseUp()

def abrir_app(programa):
    os.system(programa)

def presentacion(direccion):
    if direccion == "siguiente":
        pyautogui.press("right")
    elif direccion == "anterior":
        pyautogui.press("left")
