#!/usr/bin/python3.9
# -*- coding=utf8 -*- 
# Creater:zhangteng
import speedtest
import urllib.request
import tkinter as tk

class Application(tk.Tk):
    def __init__(self):
        super.__init__()
        self.title('测试网速')
        self.geometry('400x200')





s = speedtest.Speedtest()
server = s.get_servers()
print(server)
server_list = s.get_best_server()

print(server_list)
dr = s.download()

up = s.upload()
print(f'下载速度：{dr /1024 /1024:.2f} Mbits')
print(f'上次速度：{up /1024 /1024:.2f} Mbits')
print('welcome to cisco live')
print('welcome to cisco live')
print('welcome to cisco live')
print('welcome to cisco live')
print('welcome to cisco live')
print('welcome to cisco live')

