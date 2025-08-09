from window import BaseWindow
from utils import *
import csv
import utils
fragment_list = ['莫妮卡','亚里莎','镜华','姬塔','露娜','真步']

middle = (680,400)
suipian_pos = (180,280)

nameBox = (666,200,1200,240)

level_times = 5
add_pos = (1240,615)

# def readCSV():
#     with open('ocr_result3.csv', encoding='utf-8') as f:
#         reader = csv.reader(f)
#         for row in reader:
#             if len(row[1]) != 2:
#                 dict[row[0]] = row[1]

#     for name in fragment_list:
#         print(dict[name])


def SweepFragment(name_text):

    name_text = name_text.replace('的记忆碎片','')
    if any(sub == name_text for sub in fragment_list):
        clickWaitImage(wait_for_image('Image/getmethod.png'))   #3
        print(f'检测到{name_text} 准备刷取')

        clickWaitImage(wait_for_image('Image/sweep.png'))   #点击 一键扫荡按钮
        time.sleep(2)
        for i in range(3):
            click(add_pos)
        
        #全部勾选
        scroll_flag = False
        while True:
            if locateCenterOnScreen('Image/pick.png') == False and scroll_flag == True:
                break

            if locateCenterOnScreen('Image/pick.png') == False:
                ag.moveTo(middle)
                ag.scroll(-200)
                scroll_flag = True
            else:
                clickWaitImage(wait_for_image('Image/pick.png'))


        clickWaitImage(wait_for_image('Image/ensure_sweep.png'))
        clickWaitImage(wait_for_image('Image/sweep_challenge.png'))

        PressUntilImage('Image/skill_increase.png',key='esc')
        time.sleep(0.5)
    click(rightPage)

def fragmentTask():
    Task = BaseWindow()
    #readCSV()

    clickWaitImage(wait_for_image('Image/flower.png'))      #1
    time.sleep(1)
    

    while True:
        click(suipian_pos)      #2
        nameImage = Task.CaptureBox(nameBox)
        name = GetText(nameImage)
        print(name)
        name_box, name_text,conf = name[0]
        SweepFragment(name_text)
        
        if utils.should_interrupt == True:
            print("中断信号触发！")
            break
        