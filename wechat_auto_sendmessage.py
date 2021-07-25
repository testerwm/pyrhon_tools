#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2021/7/24 4:28 下午
# @Author  : 山西_王二狗
# @Site    : 
# @File    : 微信自动发送.py
# @Software: PyCharm

import time
from pynput.keyboard import  Key, Controller as key_cl # 键盘的控制器
from pynput.mouse import Button, Controller as mouse_cl  # 鼠标的控制器


# 键盘的控制函数

def keyboard_input(string):
    keyboard = key_cl() # 获取鼠标的权限
    keyboard.type(string) # 设置数据的类型

# 鼠标的控制函数

def mouse_click():
    mouse = mouse_cl() # 获取鼠标的权限
    mouse.press(Button.left) # 模拟鼠标左键的按下
    mouse.release(Button.left) # 模拟鼠标左键的弹起


# 实现消息的发送
def send_message(number, string):
    print("程序在三秒钟之后开始执行")
    time.sleep(3)
    keyboard = key_cl()

    for i in range(number):
        keyboard_input(string)
        mouse_click()
        time.sleep(2)

        keyboard.press(Key.enter)# 模拟回车键的按下

        keyboard.release(Key.enter)# 模拟回车键的弹起

if __name__=="__main__":
    send_message(1, '你大点声，看不到你的文字！！！！ 你的手速不行')
    send_message(1, 'i dont know !')