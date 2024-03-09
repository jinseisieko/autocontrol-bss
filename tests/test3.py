from time import sleep

import win32gui

# Получить дескриптор окна для рабочего стола
hwnd = win32gui.FindWindow(None, "Roblox")

# Получить контекст устройства для рабочего стола
dc = win32gui.GetDC(hwnd)
sleep(1)
# Нарисовать прямоугольник на рабочем столе
win32gui.Rectangle(dc, 100, 100, 200, 200)
sleep(3)
# Освободить контекст устройства
win32gui.ReleaseDC(hwnd, dc)