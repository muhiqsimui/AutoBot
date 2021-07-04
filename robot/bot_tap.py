
from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api
import win32con

# pyautogui.displayMousePosition()

# Tile 1 Position: X:  581 Y:  400 RGB: ( 77,  80, 115)
# Tile 2 Position: X:  682 Y:  400 RGB: (  0,   0,   0)
# Tile 3 Position: X:  770 Y:  400 RGB: ( 79,  82, 116)
# Tile 4 Position: X:  869 Y:  400 RGB: ( 80,  83, 116)


def tap(x, y):
    win32api.SetCursorPos((x, y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    time.sleep(0.05)  # This pauses the script for 0.01 seconds
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)


while keyboard.is_pressed('q') == False:
    #kordinat x y
    h = 791
    x1 = 427
    y1 = h
    x2 = 565
    y2 = h
    x3 = 724
    y3 = h
    x4 = 853
    y4 = h

    #tekan jika warna = 0 = hitam rgb(0,0,0)
    if pyautogui.pixel(x1, y1)[0] == 0:
        tap(x1, y1)
    if pyautogui.pixel(x2, y2)[0] == 0:
        tap(x2, y2)
    if pyautogui.pixel(x3, y3)[0] == 0:
        tap(x3, y3)
    if pyautogui.pixel(x4, y4)[0] == 0:
        tap(x4, y4)
