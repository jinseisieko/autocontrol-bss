import win32gui
import win32con
from time import sleep

# Получить дескриптор окна для рабочего стола
hwnd = win32gui.FindWindow(None, "Roblox")

# Получить контекст устройства для рабочего стола
dc = win32gui.GetDC(hwnd)
sleep(1)

# Нарисовать прямоугольник на рабочем столе
win32gui.Rectangle(dc, 100, 100, 200, 200)

# Изменить порядок отображения окна рабочего стола
win32gui.SetWindowPos(hwnd, win32con.HWND_TOPMOST, 0, 0, 0, 0, win32con.SWP_NOMOVE | win32con.SWP_NOSIZE)
sleep(3)

# Освободить контекст устройства
win32gui.ReleaseDC(hwnd, dc)