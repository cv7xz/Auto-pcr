from window import BaseWindow
from utils import *

import utils
icon_event = (1300,300)
middle = (680,400)
skip = (1230,125)

risk_icon = (675,746)
state = 'mainpage'

def riskReturn():
    click(risk_icon)
    clickWaitImage(wait_for_image('Image/ToRisk.png'))
    clickWaitImage(wait_for_image('Image/return.png'),time2=8)
    clickWaitImage(wait_for_image('Image/skip_over.png'))
    clickWaitImage(wait_for_image('Image/reRisk.png'))
    clickWaitImage(wait_for_image('Image/go.png'))
    PressUntilImage('Image/mainpage_flag.png',key='esc')

def riskTask():
    state = 'mainpage'
    while True:
        if utils.should_interrupt == True:
            print("中断信号触发！")
            break

        if state == 'mainpage':
            click(icon_event)
            time.sleep(1)
            click(middle)
            if locateCenterOnScreen('Image/door.png'):
                state == 'risk'
            
            else:
                state = 'other'

        elif state == 'risk':
            clickWaitImage(wait_for_image('Image/door.png'),times=2)
            image_result = clickUntilImages(['Image/door.png','Image/mainpage_flag.png'],skip)
            time.sleep(10)
            if image_result == 0:
                state = 'risk'    #
            elif image_result == 1:
                state = 'mainpage'
        
        elif state == 'other':
            clickUntilImage('Image/mainpage_flag.png',skip)
            state = 'mainpage'
