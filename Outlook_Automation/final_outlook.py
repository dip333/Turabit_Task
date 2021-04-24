import pyautogui
import time
from PIL import Image
import sys
from os import path
import cv2
import numpy as np
import os, glob, shutil

def get_path():
    if getattr(sys, 'frozxen', False) and hasattr(sys, '_MEIPASS'):
        print('running in a PyInstaller bundle')
        return getattr(sys, '_MEIPASS', path.abspath(path.dirname(__file__)))
    else:
        print('running in a normal Python process')
        return getattr(sys, '_MEIPASS', path.abspath(path.dirname(__file__)))

bash_path = get_path()
pyautogui.PAUSE = 1.5
pyautogui.FAILSAFE = False
f = open("status.txt", "w+")
f.truncate()

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

copy_dir(f"{bash_path}\\img","C:/outlook/")

def detect(img,template):
    # large = pyautogui.screenshot("my_screenshot.png")
    large_image = Image.open(img).convert('LA')
    large_image.save("large_gray.png")
    # small = cv2.imread(template)
    small_image = Image.open(template).convert('LA')
    small_image.save("small_gray.png")

    img = cv2.imread(img,0)
    template = cv2.imread(template,0)
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
        centerx = (top_left[0] + bottom_right[0]) / 2
        centery = (top_left[1] + bottom_right[1]) / 2
        print("center coordinates are ", centerx, centery)
        pyautogui.click(centerx, centery)
        # os.remove("small_gray.png")
        # os.remove(".\\img\\screenshot.png")
        # os.remove("large_gray.png")

#
# pyautogui.hotkey('win', 'r')
# pyautogui.write("outlook.exe /safe")
# pyautogui.press('enter')
# time.sleep(3)
# pyautogui.press('enter')

pyautogui.press('win')
pyautogui.write('outlook')
f.write("Typing outlook \n")
time.sleep(2)

img=pyautogui.screenshot(".\\img\\screenshot.png")
copy_dir(f"{bash_path}\\img","C:/outlook/")
detect("C:\outlook\screenshot.png","C:\outlook\outlook.png")
os.remove("C:\outlook\screenshot.png")
f.write("Clicked on outlook \n")
time.sleep(9)

def main():
    try:
        x, y = pyautogui.locateCenterOnScreen("C://outlook//popup.png")
        print(x)
        time.sleep(2)
        f.write("Running close \n")
        if (x != 0):
            img = pyautogui.screenshot(".\\img\\screenshot.png")
            copy_dir(f"{bash_path}\\img", "C:/outlook/")
            detect("C:\outlook\screenshot.png", "C:\\outlook\\close.png")
            os.remove("C:\outlook\screenshot.png")
            time.sleep(3)
            f.write("Clicked on close \n")
        else:
            pass
    except:
        print("popup not found")
    finally:
            img = pyautogui.screenshot(".\\img\\screenshot.png")
            copy_dir(f"{bash_path}\\img", "C:/outlook/")
            detect("C:\outlook\screenshot.png", "C:\\outlook\\file.png")
            os.remove("C:\outlook\screenshot.png")
            f.write("Clicked on file \n")
            time.sleep(3)

            img = pyautogui.screenshot(".\\img\\screenshot.png")
            copy_dir(f"{bash_path}\\img", "C:/outlook/")
            detect("C:\outlook\screenshot.png", "C:\outlook\option.png")
            os.remove("C:\outlook\screenshot.png")
            f.write("Clicked on option \n")
            time.sleep(3)

            img = pyautogui.screenshot(".\\img\\screenshot.png")
            copy_dir(f"{bash_path}\\img", "C:/outlook/")
            detect("C:\outlook\screenshot.png", "C:\outlook\mail.png")
            os.remove("C:\outlook\screenshot.png")
            f.write("Clicked on mail \n")
            time.sleep(3)

            img = pyautogui.screenshot(".\\img\\screenshot.png")
            copy_dir(f"{bash_path}\\img", "C:/outlook/")
            detect("C:\outlook\screenshot.png", "C:\outlook\sign.png")
            os.remove("C:\outlook\screenshot.png")
            f.write("Clicked on sign \n")
            time.sleep(4)

            img = pyautogui.screenshot(".\\img\\screenshot.png")
            copy_dir(f"{bash_path}\\img", "C:/outlook/")
            detect("C:\outlook\screenshot.png", "C:\\outlook\\new.png")
            os.remove("C:\outlook\screenshot.png")
            f.write("Clicked on new \n")
            pyautogui.write("abc")
            pyautogui.press('enter')
            pyautogui.click(692, 623)
            pyautogui.write("Hello")
            time.sleep(3)

            img = pyautogui.screenshot(".\\img\\screenshot.png")
            copy_dir(f"{bash_path}\\img", "C:/outlook/")
            detect("C:\outlook\screenshot.png", "C:\outlook\ok.png")
            os.remove("C:\outlook\screenshot.png")
            f.write("Clicked on ok \n")
            time.sleep(3)

            img = pyautogui.screenshot(".\\img\\screenshot.png")
            copy_dir(f"{bash_path}\\img", "C:/outlook/")
            detect("C:\outlook\screenshot.png", "C:\outlook\ok2.png")
            os.remove("C:\outlook\screenshot.png")
            f.write("Clicked on ok2 \n")
            time.sleep(3)

            # rem_dir("C:/outlook")

#2nd method

# pyautogui.press('win')
# pyautogui.write('outlook')
# f.write("Typing outlook \n")
# time.sleep(2)
#
# print(path.exists("C://outlook//outlook.png"))
# outlook = pyautogui.locateCenterOnScreen("C://outlook//outlook.png")
# print(outlook)
# pyautogui.click(outlook)
# f.write("clicked on outlook \n")
# time.sleep(6)
#
# def main():
#     try:
#         x, y = pyautogui.locateCenterOnScreen("C://outlook//popup.png")
#         print(x)
#         f.write("Running close \n")
#         if (x != 0):
#             pyautogui.click(x, y)
#             time.sleep(3)
#         else:
#             pass
#     except:
#         print("popup not found")
#     finally :
#         print(path.exists("C://outlook//file.png"))
#         file = pyautogui.locateCenterOnScreen("C://outlook//file.png")
#         print(file)
#         pyautogui.click(file)
#         f.write("opening file \n")
#         time.sleep(3)
#
#         print(path.exists("C://outlook//option.png"))
#         option = pyautogui.locateCenterOnScreen("C://outlook//option.png")
#         print(option)
#         pyautogui.click(option)
#         time.sleep(3)
#         f.write("opening option \n")
#
#         print(path.exists("C://outlook//mail.png"))
#         mail = pyautogui.locateCenterOnScreen("C://outlook//mail.png")
#         print(mail)
#         pyautogui.click(mail)
#         time.sleep(3)
#         f.write("opening mail \n")
#
#         print(path.exists("C://outlook//sign.png"))
#         sign = pyautogui.locateCenterOnScreen("C://outlook//sign.png")
#         print(sign)
#         pyautogui.click(sign)
#         time.sleep(3)
#         f.write("opening sign \n")
#
#         print(path.exists("C://outlook//new.png"))
#         x,y = pyautogui.locateCenterOnScreen("C://outlook//new.png")
#         print("Point(x=",x,"y=",y,")")
#         pyautogui.click(x,y)
#
#         time.sleep(3)
#         f.write("opening new sign \n")
#
#         pyautogui.write('abc')
#         pyautogui.press('enter')
#         pyautogui.click(x,y+150)
#         pyautogui.write("Hello")
#         time.sleep(3)
#
#         print(path.exists("C://outlook//ok.png"))
#         ok = pyautogui.locateCenterOnScreen("C://outlook//ok.png")
#         print(ok)
#         pyautogui.click(ok)
#         time.sleep(3)
#         f.write("clicking ok \n")
#
#         print(path.exists("C://outlook//ok2.png"))
#         ok = pyautogui.locateCenterOnScreen("C://outlook//ok2.png")
#         print(ok)
#         pyautogui.click(ok)
#         time.sleep(3)
#         f.write("clicking ok 2\n")
#
#         rem_dir("C:/outlook")

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Keyboard Interrupted')
        sys.exit(0)


