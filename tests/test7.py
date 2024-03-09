from time import sleep

import win32con
import win32gui
import win32ui


def get_window_fps(hwnd):
    """Возвращает частоту кадров указанного окна."""
    hdc = win32gui.GetDC(hwnd)
    gdi = win32ui.CreateDCFromHandle(hdc)
    fps = gdi.GetDeviceCaps(win32con.VREFRESH)
    win32gui.ReleaseDC(hwnd, hdc)
    return fps


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
    print(get_window_fps(hwnd))
    sleep(1 / (get_window_fps(hwnd)))  # 60 кадров в секунду
