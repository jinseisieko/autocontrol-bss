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


# Получить дескриптор окна
hwnd = win32gui.GetForegroundWindow()
while True:
    # Получить частоту кадров окна
    fps = get_window_fps(hwnd)

    # Вывести частоту кадров
    print(f"Частота кадров окна: {fps} кадров в секунду")
