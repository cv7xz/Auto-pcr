import win32gui,win32con

import pyautogui as ag
import time
from typing import *
from pyscreeze import Box

import easyocr
import keyboard

icon = (220,600)
normal = (820,160)
hard = (1000,160)
vhard = (1150,160)

mainpage = (125,750)

leftPage = (50,415)
rightPage = (1300,415)

should_interrupt = False
def ContinueClick(pos,duration):
    starttime = time.time()
    while(time.time()-starttime < duration):
        click(pos)
        time.sleep(0.7)

def ContinueClick_aixY(posx,ymin,ymax,duration):
    starttime = time.time()
    currenty = ymin
    while(time.time()-starttime < duration):
        currenty += 10
        if currenty > ymax:
            currenty = ymin

        click(posx,currenty)
        time.sleep(0.2)


def clickWaitImage(condition,pos=-1,time2 = 30,times = 1):
    """等待直到满足条件后点击"""
    Image_box = wait_until(condition,timeout = time2)
    if Image_box:
        if pos == -1:
            for i in range(times):
                time.sleep(1)
                click(Image_box)
        else:
            for i in range(times):
                time.sleep(1)
                click(pos)

def clickUntilImage(image,pos,times = 15,interval = 0.3):
    Image_box = locateCenterOnScreen(image,confidence=0.6)
    if times <= 0:
        return
    if should_interrupt == True:
        return
    if Image_box == False:

        click(pos)
        time.sleep(interval)
        clickUntilImage(image,pos,times-1)

    else:
        print(f"找到目标图像 不再click {pos}")

def clickUntilImages(images,pos,times = 15):


    if times <= 0:
        return
    if should_interrupt == True:
        return
    
    for index,image in enumerate(images):
        image_box = locateCenterOnScreen(image)
        if image_box == False:
            if index + 1 == len(images):
                time.sleep(1)
                clickUntilImages(images,pos,times-1)
            continue
            
        else:
            print(f"找到目标图像{image} 不再click {pos}")
            return index

#重复 直到出现某个图像
def PressUntilImage(image,key,times=15):
    Image_box = locateCenterOnScreen(image,confidence=0.6)

    if times <= 0:
        return
    
    if should_interrupt == True:
        return
    
    if Image_box == False:
        ag.press(key)
        time.sleep(2)
        PressUntilImage(image,key,times-1)

    else:
        print(f"找到目标图像 不再Press {key}")

def PressWaitImage(condition,key='esc',time2 = 30,times = 1):
    """等待直到满足条件后点击"""
    Image_box = wait_until(condition,timeout = time2)
    if Image_box:
        for i in range(times):
            time.sleep(1)
            ag.press(key)

def wait_until(condition_func, timeout=40, interval=1):
    """重复检查 condition_func 是否满足条件，返回坐标或 None"""
    start_time = time.time()
    while time.time() - start_time < timeout:
        if should_interrupt == True:
            return None

        location = condition_func()
        if location:            
            return location
        
        time.sleep(interval)
    print("已超时 未找到图片")
    return None


def wait_for_image(path):
    return lambda: locateCenterOnScreen(path,confidence=0.6)


def wait_for_image_list(pathlist):

    def posibleImage():
        for path in pathlist:
            location = locateCenterOnScreen(path,show = False)
            if location:
                print(f'多图片寻找 发现{path} {location}')
                return location

        return False

    return posibleImage


def click(clickpos):
    pos = ag.position()
    ag.click(clickpos)
    time.sleep(0.02)
    ag.moveTo(pos)

#返回更合理  找到返回坐标  找不到返回False
def locateCenterOnScreen(path,confidence=0.6,show = True):
    try:
        loc = ag.locateCenterOnScreen(path,confidence=0.8)
        if show:
            print(f'发现图片 {loc}')
        return loc
    except:
        print(f'未找到 {path}')
        return False

#根据路径或者图片 获取文字（参数传哪个都可以）
def GetText(filename):
    reader = easyocr.Reader(['ch_sim', 'en'])
    results = reader.readtext(filename)

    for bbox, text, confidence in results:
        print(bbox, text, confidence)

    return results


        