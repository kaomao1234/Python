import cv2
import numpy as np
import win32gui
import win32con
from PIL import ImageGrab


def get_window_rect(hwnd):
    rect = win32gui.GetWindowRect(hwnd)
    x, y, w, h = rect
    return x, y, w - x, h - y


window_title = "Task Manager"
hwnd = win32gui.FindWindow(None, window_title)

if hwnd == 0:
    print("Window not found.")
else:
    x, y, w, h = get_window_rect(hwnd)

    while True:
        hwnd_dc = win32gui.GetWindowDC(hwnd)
        mfc_dc = win32gui.CreateCompatibleDC(hwnd_dc)
        bmp = win32gui.CreateCompatibleBitmap(hwnd_dc, w, h)
        win32gui.SelectObject(mfc_dc, bmp)
        win32gui.BitBlt(mfc_dc, 0, 0, w, h, hwnd_dc, 0, 0, win32con.SRCCOPY)

        screenshot = np.array(ImageGrab.grab(bbox=(x, y, x + w, y + h)))
        screenshot = cv2.cvtColor(screenshot, cv2.COLOR_RGB2BGR)

        cv2.imshow("Screen Recording", screenshot)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

cv2.destroyAllWindows()
