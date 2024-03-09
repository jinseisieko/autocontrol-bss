import win32con
import win32gui


def on_click(hwnd, x, y, flags):
    # Сделать что-то при нажатии на координаты (x, y) в окне с дескриптором hwnd
    print("Нажато на координаты ({}, {}) в окне с дескриптором {}".format(x, y, hwnd))


def main():
    # Получить дескриптор окна
    hwnd = win32gui.FindWindow(None, "Заголовок окна")

    # Установить хук на событие нажатия мыши
    win32gui.SetWindowsHookEx(win32con.WH_MOUSE_LL, on_click, None, 0)

    # Запустить цикл сообщений
    win32gui.PumpMessages()


if __name__ == "__main__":
    main()
