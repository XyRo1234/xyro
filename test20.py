from faulthandler import disable
import re
import os
from tkinter import * # __all__
from tkinter import filedialog
import tkinter as tk
from tkinter import PhotoImage, Button, Label, StringVar, ttk, colorchooser
import tkinter.ttk as ttk
import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import sys
import requests
from bs4 import BeautifulSoup as bs


root = Tk()
root.title("Pronounce Replace")
# root.geometry("640x480+300+100") # 가로 * 세로 + x좌표 + y좌표


# 파일선택 추가
def add_file():
    files = filedialog.askopenfilenames(title="이미지 파일을 선택하세요", \
        filetypes=(("tmx", "*.tmx"), ("모든 파일", "*.*")), \
        initialdir=r"D:\aa")
        # 최초에 사용자가 지정한 경로를 보여줌
    
    # 사용자가 선택한 파일 목록
    for file in files:
        list_file.insert(END, file)

# 선택 삭제
def del_file():
    #print(list_file.curselection())
    for index in reversed(list_file.curselection()):
        list_file.delete(index)


def start():
    text = rdoVar.get()
    print(text)
    for file in list_file.get(0, END):
        print(file)





# 파일 프레임 (파일 추가, 선택 삭제)


rdoVar = StringVar()
rdobtn1 = Radiobutton(root, text='en-GB', value='en-GB', variable=rdoVar)
rdobtn2 = Radiobutton(root, text='en-US', value='en-US', variable=rdoVar)
rdobtn1.invoke()
rdobtn1.grid(row=0, column=2, padx=100, pady=5, sticky=N+E+W+S)
rdobtn2.grid(row=1, column=2, padx=100, pady=5, sticky=N+E+W+S)

file_frame = LabelFrame(root, text="파일선택")
file_frame.grid(row=2, column=2, padx=100, pady=5, sticky=N+E+W+S)

btn_add_file = Button(file_frame, padx=5, pady=5, width=12, text="파일추가", command=add_file)
btn_add_file.pack(side="left")

btn_del_file = Button(file_frame, padx=5, pady=5, width=12, text="선택삭제", command=del_file)
btn_del_file.pack(side="right")

# 리스트 프레임
list_frame = Frame(root)
list_frame.grid(row=3, column=2, padx=5, pady=5, sticky=E+W)

lab1 = Label(list_frame)
lab1.config(text = "언어코드필수 tmx파일")
lab1.pack()

scrollbar = Scrollbar(list_frame)
scrollbar.pack(side="right", fill="y")

list_file = Listbox(list_frame, selectmode="extended", height=15, yscrollcommand=scrollbar.set)
list_file.pack(side="left", fill="both", expand=True)
scrollbar.config(command=list_file.yview)


# 실행 프레임
frame_run = Frame(root)
frame_run.grid(row=6, column=2, sticky=N+E+W+S)

btn_close = Button(frame_run, padx=5, pady=5, text="닫기", width=12, command=root.quit)
btn_close.pack(side="right", padx=5, pady=5)

btn_start = Button(frame_run, padx=5, pady=5, text="시작", width=12, command=start)
btn_start.pack(side="right", padx=5, pady=5)


root.resizable(True, False) # x(너비), y(높이) 값 변경 불가 (창 크기 변경 불가)
root.mainloop()
