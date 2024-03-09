from time import sleep

import win32gui
import win32api
import win32con

# Найти окно по имени
window_name = "autocontrol-bss – main.py"
# hwnd = win32gui.FindWindow(None, window_name)
hwnd = win32gui.GetForegroundWindow()
print(hwnd)

# Получить дескриптор окна
window_handle = win32gui.GetDlgCtrlID(hwnd)

# Нажать кнопку
win32api.PostMessage(window_handle, win32con.BM_CLICK, 1338, 40)
win32api.mouse_event(0x02, 284, 42, 0, 0)
win32api.mouse_event(0x04, 284, 42, 0, 0)
sleep(2)
print(win32api.GetCursorPos())