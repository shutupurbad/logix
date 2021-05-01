from pyautogui import *
import pyautogui
import time
from pynput.keyboard import Key, Controller
import random
import os
import win32api, win32con

keyboard = Controller()
call = "img.png"
avatar = "img1.png"
pgui = pyautogui

while 1:
    if pyautogui.locateOnScreen("img.png", grayscale=True, confidence=0.8) != None:
        if pyautogui.locateOnScreen("img1.png") != None:
            pgui.click("img1.png")
            time.sleep(0.5)
            try:
                pyautogui.click(avatar)
            except:
                pass
            try:
                pyautogui.click(call)
            except:
                pass
    else:
        pass
