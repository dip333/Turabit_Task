import pyautogui
import time,sys
from os import path

def get_path():
    if getattr(sys, 'frozen', False) and hasattr(sys, '_MEIPASS'):
        print('running in a PyInstaller bundle')
        return getattr(sys, '_MEIPASS', path.abspath(path.dirname(__file__)))
    else:
        print('running in a normal Python process')
        return getattr(sys, '_MEIPASS', path.abspath(path.dirname(__file__)))

bash_path = get_path()
pyautogui.PAUSE = 1.5
pyautogui.FAILSAFE = False

pyautogui.hotkey('win', 'r')
pyautogui.write("outlook.exe /safe")
pyautogui.press('enter')
time.sleep(3)
pyautogui.press('enter')
