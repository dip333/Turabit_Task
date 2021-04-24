import pyautogui
import time
from PIL import Image
import sys
from os import path
import cv2
import numpy as np
import os, glob, shutil


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

def make_dir(path):
    if not os.path.isdir(path):
        os.mkdir(path)

def copy_dir(source_item, destination_item):
    if os.path.isdir(source_item):
        make_dir(destination_item)
        sub_items = glob.glob(source_item + '/*')
        for sub_item in sub_items:
            copy_dir(sub_item, destination_item + '/')
    else:
        shutil.copy(source_item, destination_item)

def rem_dir(destination_item):
   shutil.rmtree(destination_item)

copy_dir(f"{bash_path}\\img","C:/notepad/")

def detect(img,template):
    # large = pyautogui.screenshot("my_screenshot.png")
    large_image = Image.open(img).convert('LA')
    large_image.save("large_gray.png")
    # small = cv2.imread(template)
    small_image = Image.open(template).convert('LA')
    small_image.save("small_gray.png")

    img = cv2.imread('large_gray.png',0)
    template = cv2.imread('small_gray.png',0)
    w, h = template.shape[::-1]
    methods = ['cv2.TM_CCOEFF']
    # methods = ['cv2.TM_CCOEFF', 'cv2.TM_CCOEFF_NORMED', 'cv2.TM_CCORR',
    #             'cv2.TM_CCORR_NORMED', 'cv2.TM_SQDIFF', 'cv2.TM_SQDIFF_NORMED']

    for meth in methods:
        method = eval(meth)
        res = cv2.matchTemplate(img, template, method)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
        if method in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]:
            top_left = min_loc
        else:
            top_left = max_loc

        bottom_right = (top_left[0] + w, top_left[1] + h)
        # print(top_left)
        # print(bottom_right)
        centerx=(top_left[0]+bottom_right[0])/2
        centery=(top_left[1]+bottom_right[1])/2
        print("center coordinates are",centerx,centery)
        # print(min_loc)
        # print(max_loc)abc.txt
        pyautogui.click(centerx,centery)
        os.remove("small_gray.png")
        os.remove(".\\img\\screenshot.png")
        os.remove("large_gray.png")

pyautogui.press('win')
pyautogui.write('notepad')
time.sleep(2)

img=pyautogui.screenshot(".\\img\\screenshot.png")
copy_dir(f"{bash_path}\\img","C:/notepad/")
detect("C:\\notepad\\screenshot.png","C:\\notepad\\notepad.png")
os.remove("C:\\notepad\\screenshot.png")
time.sleep(3)

img=pyautogui.screenshot(".\\img\\screenshot.png")
copy_dir(f"{bash_path}\\img","C:/notepad/")
detect("C:\\notepad\\screenshot.png","C:\\notepad\\file.png")
os.remove("C:\\notepad\\screenshot.png")

time.sleep(3)

img=pyautogui.screenshot(".\\img\\screenshot.png")
copy_dir(f"{bash_path}\\img","C:/notepad/")
detect("C:\\notepad\\screenshot.png","C:\\notepad\\save as.png")
os.remove("C:\\notepad\\screenshot.png")
time.sleep(3)

pyautogui.write("abc.txt")
pyautogui.press("enter")
time.sleep(3)

rem_dir("C:/notepad")

#
# notepad = pyautogui.locateCenterOnScreen(get_path() + r'//notepad.png')
# print(notepad)
# pyautogui.click('notepad.png')
# pyautogui.write("HELLO")
# time.sleep(3)
# print(path.exists(bash_path + "//file.png"))
# file = pyautogui.locateCenterOnScreen(get_path() + r'//file.png')
# print(file)
# pyautogui.click('file.png')
# time.sleep(3)
# print(path.exists(bash_path + "//save as.png"))
# save = pyautogui.locateCenterOnScreen(get_path() + r'//save as.png')
# print(save)
# pyautogui.click('save as.png')
# pyautogui.write('abc.txt')
# pyautogui.press('enter')