import win32con
import win32gui


def is_window_maximized(hwnd: int) -> bool:
    """
    Checks if the window is maximized.

    Args:
        hwnd (int): The window handle.

    Returns:
        bool: True if the window is maximized, False otherwise.
    """
    style = win32gui.GetWindowLong(hwnd, win32con.GWL_STYLE)
    return style & win32con.WS_MAXIMIZE == win32con.WS_MAXIMIZE


def maximize_window(hwnd: int) -> None:
    """
    Maximize the window with the given handle.

    Args:
        hwnd (int): The window handle.
    """
    win32gui.ShowWindow(hwnd, win32con.SW_MAXIMIZE)