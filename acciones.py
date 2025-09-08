import os
import webbrowser
import pyautogui

def abrir_navegador():
    webbrowser.open("https://www.google.com")

def abrir_musica():
    os.system("start chrome")  # En Windows (puedes cambiar por otra app)

def mover_mouse(x, y):
    pyautogui.moveTo(x, y)

def click_mouse():
    pyautogui.click()
