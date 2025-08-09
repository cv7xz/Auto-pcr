from window import BaseWindow
from utils import *

import utils

all = (1215,218)
update = (782,652)
buy_all = (1215,652)

def buyTask():
    for i in range(5):
        click(all)
        click(buy_all)
        clickWaitImage(wait_for_image('Image/ensure.png'))
        time.sleep(2)
        clickWaitImage(wait_for_image('Image/ensure.png'))
        time.sleep(1)
        click(update)
        clickWaitImage(wait_for_image('Image/ensure.png'))
        time.sleep(1)