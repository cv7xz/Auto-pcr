from window import BaseWindow
from utils import *

import utils
def OpenGame():
    Task = BaseWindow()
    mumu = Task.GetWindowFromTitle("MuMu模拟器12")

    Task.SetWindow(mumu)
    ag.click(icon)
    clickWaitImage(wait_for_image('Image/button.png'),icon,time2 = 100)

    startTime = time.time()
    while time.time() - startTime < 40:
        if utils.should_interrupt == True:
            break
        clickWaitImage(wait_for_image_list(['Image/close.png','Image/cancel.png','Image/skip.png']))


def DailyTask():
    clickWaitImage(wait_for_image('Image/daily.png'))
    clickWaitImage(wait_for_image('Image/auto.png'))

    startTime = time.time()
    while time.time() - startTime < 40:
        if utils.should_interrupt == True:
            break
        clickWaitImage(wait_for_image_list(['Image/kekeluo.png','Image/ensure.png','Image/ensure2.png','Image/close.png']))

    clickWaitImage(wait_for_image('Image/dailyclose.png'))