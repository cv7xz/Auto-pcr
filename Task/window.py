import win32gui,win32con

import pyautogui as ag
from typing import *
from pyscreeze import Box
from PIL import ImageGrab
from utils import *
import numpy as np
class BaseWindow:
    def __init__(self):
        pass
    #通过标题字符寻找窗口
    def GetWindowFromTitle(self,title):
        hwnd = win32gui.FindWindow(None, title)
        print(f"{title} id: {hwnd}")
        return hwnd

    #打印所有有效窗口标题
    def CheckAllWindows(self,):
        def enum_handler(hwnd, result_list):
            if win32gui.IsWindowVisible(hwnd):
                title = win32gui.GetWindowText(hwnd)
                if title:
                    result_list.append((hwnd, title))

        windows = []
        win32gui.EnumWindows(enum_handler, windows)
        for hwnd, title in windows:
            print(f"{hwnd}: {title}")


    #获取窗口的坐标
    def GetWindowPosition(self,hwnd):
        left, top, right, bottom = win32gui.GetWindowRect(hwnd)
        print(left, top, right, bottom)  

    #设置窗口的坐标
    def SetWindow(self,hwnd):
        win32gui.SetWindowPos(
            hwnd,
            win32con.HWND_TOP,  # 窗口 Z 序位置
            0,0,1350,800,         
            0
        )
    
    def CaptureWindow(self,hwnd,filename = None):
        box = win32gui.GetWindowRect(hwnd)
        
        img = ImageGrab.grab(box)
        if filename != None:
            img.save(filename)
        return img
    
    def CaptureBox(self,box,filename=None):
        img = ImageGrab.grab(box)
        if filename != None:
            img.save(filename)
            
        img_np = np.array(img)
        return img_np