from window import BaseWindow
from utils import *


risk_icon = (677,753)
battle_point = (1223,666)

def enter_jjc1():
    clickWaitImage(wait_for_image('Image/jjc1.png'))

    clickUntilImage(wait_for_image('image/battle_skip.png'),battle_point)
    clickWaitImage(wait_for_image('image/battle_skip.png'))
    clickWaitImage(wait_for_image('image/next_step.png'))

    PressWaitImage(wait_for_image('Image/jjc_flag.png'))
    
def enter_jjc2():
    clickWaitImage(wait_for_image('Image/jjc2.png'))

    clickUntilImage(wait_for_image('image/battle_skip.png'),battle_point)
    clickWaitImage(wait_for_image('image/battle_skip.png'))

    clickWaitImage(wait_for_image('image/next_step.png'))

    PressWaitImage(wait_for_image('Image/jjc_flag.png'))

def jjcTask():
    click(risk_icon)

    clickWaitImage(wait_for_image('Image/jjc.png'))
    enter_jjc1()
    time.sleep(0.5)
    ag.press(keys='esc')
    enter_jjc2()
