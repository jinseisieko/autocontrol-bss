import win32gui
import win32con
from time import sleep

# Получить дескриптор окна для рабочего стола
hwnd = win32gui.FindWindow(None, "Roblox")

# Получить контекст устройства для рабочего стола
dc = win32gui.GetDC(hwnd)

# Цикл для постоянного обновления содержимого окна
while True:
    # Нарисовать прямоугольник на рабочем столе
    win32gui.Rectangle(dc, 100, 100, 200, 200)

    # Обновить содержимое окна
    win32gui.InvalidateRect(hwnd, None, False)
    win32gui.UpdateWindow(hwnd)

    # Задержка для имитации частоты кадров
    sleep(1 / 60)  # 60 кадров в секунду
