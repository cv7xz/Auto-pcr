import tkinter as tk
from tkinter import ttk

import threading
import DailyTask
import jjcTask
import suipianTask
import riskTask
import BuyTask
import keyboard,time
import utils
# 定义不同方案对应的按钮内容


def set_interrupt_true():
    utils.should_interrupt = True
    print("已设置中断信号")

def set_interrupt_false():
    utils.should_interrupt = False
    print("恢复自动")

def reset_interrupt():
    set_interrupt_false()
    threading.Timer(3,set_interrupt_true).start()

def monitor_interrupt_key():
    while True:
        if keyboard.is_pressed('esc'):
            utils.should_interrupt = True
            print("中断信号触发！")
            break
        time.sleep(0.1)

scheme_actions = {
    "启动游戏": {"启动": DailyTask.OpenGame},
    "每日日常": {"日常": DailyTask.DailyTask},
    "碎片获取": {"碎片": suipianTask.fragmentTask},
    "竞技场": {"竞技场":jjcTask.jjcTask,"jjc1":jjcTask.enter_jjc1,"jjc2":jjcTask.enter_jjc2},
    "冒险收菜": {"收菜":riskTask.riskReturn,"事件": riskTask.riskTask},
    "购买":{"买经验药水":BuyTask.buyTask},
    "操作处理": {"中断": set_interrupt_true, "恢复": set_interrupt_false,"重置":reset_interrupt()},
}

def thread_func(f):           #闭包问题 ?
    t = threading.Thread(target=f)
    t.daemon = True
    t.start()

def show_buttons_for_scheme(scheme_name):
    # 清空中间区域已有的按钮
    for widget in center_frame.winfo_children():
        widget.destroy()

    for btn_text,func in scheme_actions[scheme_name].items():
        btn = ttk.Button(center_frame,
                        text=btn_text,
                        command = lambda fu = func: thread_func(fu)
                        )
        btn.pack(pady=5)

# 创建主窗口
root = tk.Tk()
root.title("多方案UI示例")
root.geometry("600x400")

# 创建左侧菜单区域
left_frame = tk.Frame(root, width=150, bg="#eeeeee")
left_frame.pack(side="left", fill="y")

# 创建中间按钮展示区域
center_frame = tk.Frame(root, bg="#f7f7f7")
center_frame.pack(side="left", fill="both", expand=True)

# 添加左侧方案按钮
for scheme_name in scheme_actions:
    btn = tk.Button(
        left_frame,
        text=scheme_name,
        width=12,
        height=1,
        command=lambda name=scheme_name: show_buttons_for_scheme(name)
    )
    btn.pack(pady=8, padx=10)


# 初始化加载第一个方案
show_buttons_for_scheme("启动游戏")

root.mainloop()
