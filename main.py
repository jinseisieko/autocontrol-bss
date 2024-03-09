import win32con
import win32gui
import cv2

def is_window_maximized(hwnd):
    """
    Проверяет, развернуто ли окно.

    Args:
        hwnd (int): Дескриптор окна.

    Returns:
        bool: True, если окно развернуто, False в противном случае.
    """
    style = win32gui.GetWindowLong(hwnd, win32con.GWL_STYLE)
    return style & win32con.WS_MAXIMIZE == win32con.WS_MAXIMIZE


def is_window_visible(hwnd):
    """
    Проверяет, видно ли окно.

    Args:
        hwnd (int): Дескриптор окна.

    Returns:
        bool: True, если окно видно, False в противном случае.
    """
    return win32gui.IsWindowVisible(hwnd)


# Получение списка всех открытых окон
windows = []
win32gui.EnumWindows(lambda hwnd, param: windows.append(hwnd), None)

# Проверка, открыто ли окно для каждого приложения
for window in windows:
    title = win32gui.GetWindowText(window)
    if is_window_visible(window):
        print(f"Окно: {title}")

print("123", win32gui.GetWindowText(win32gui.GetForegroundWindow()))
import Сhecks.functions as fc
h = win32gui.FindWindow(None, "Roblox")
fc.maximize_window(h)
image = win32gui.GetDC(h)
cv2.imwrite("image.png", image)