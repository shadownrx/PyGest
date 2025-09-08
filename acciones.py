import pyautogui
import os

def mover_mouse(x, y, ancho, alto):
    """
    Mueve el mouse en proporción a la pantalla.
    """
    screen_w, screen_h = pyautogui.size()
    new_x = int(x / ancho * screen_w)
    new_y = int(y / alto * screen_h)
    pyautogui.moveTo(new_x, new_y)


def click_mouse():
    """
    Clic izquierdo.
    """
    pyautogui.click()


def click_derecho():
    """
    Clic derecho.
    """
    pyautogui.rightClick()


def hacer_scroll(direccion):
    """
    Scroll hacia arriba o abajo.
    """
    if direccion == "arriba":
        pyautogui.scroll(100)
    elif direccion == "abajo":
        pyautogui.scroll(-100)


def drag_mouse(accion):
    """
    Drag con el mouse (mantener y soltar).
    """
    if accion == "down":
        pyautogui.mouseDown()
    elif accion == "up":
        pyautogui.mouseUp()


def abrir_bloc_notas():
    """
    Abre Bloc de notas en Windows.
    """
    os.system("notepad")


def abrir_navegador():
    """
    Abre navegador (Chrome en este ejemplo).
    """
    os.system("start chrome")
