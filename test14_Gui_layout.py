
from cgitb import text
from tkinter import *
import tkinter as tk
from tkinter import PhotoImage, Button, Label, StringVar, ttk, colorchooser
import tkinter.ttk as ttk
import tkinter.messagebox as msgbox
from tkinter import * # __all__
from tkinter import filedialog
import json
import os
from turtle import width
import pandas as pd
from pyairtable import Table
import re
import numpy

root = Tk()
root.title("Airtable API")
#root.geometry("640x480+300+100") # 가로 * 세로 + x좌표 + y좌표


# 파일 추가
def add_file():
    pass

# 선택 삭제
def del_file():
    pass

# 저장 경로 (폴더)
def browse_dest_path():
    pass

def srt_ssml_create(path):
    pass

def start_1():
    pass

def start_2():
    pass
    
def GMDS_Data():
    pass



# 저장 경로 프레임                                                                              # 0,0
path_frame = LabelFrame(root, text="저장경로")
path_frame.grid(row=0, column=0, padx=5, pady=5, sticky=N+E+W+S)


txt_dest_path = Entry(path_frame)
txt_dest_path.pack(side="left", fill="x", expand=True, padx=5, pady=5, ipady=4) # 높이 변경

btn_dest_path = Button(path_frame, text="찾아보기", width=10, command=browse_dest_path)
btn_dest_path.pack(side="right", padx=5, pady=5)


# 진행 상황 Progress Bar
frame_progress = LabelFrame(root, text="진행상황")
frame_progress.grid(row=2, column=0, padx=5, pady=5, sticky=E+W)

p_var = DoubleVar()
progress_bar = ttk.Progressbar(frame_progress, maximum=100, variable=p_var)
progress_bar.pack(fill="x", padx=5, pady=5)


# 실행 프레임
frame_run = Frame(root)
frame_run.grid(row=3, column=0)

btn_close = Button(frame_run, padx=5, pady=5, text="닫기", width=12, command=root.quit)
btn_close.pack(side="right", padx=5, pady=5)

btn_start = Button(frame_run, padx=5, pady=5, text="시작", width=12, command=start_1)
btn_start.pack(side="right", padx=5, pady=5)



label = Label(root).grid(row=0, column=3,ipadx=20)


# 파일 프레임 (파일 추가, 선택 삭제)                                                                # 0,4
file_frame = LabelFrame(root, text="파일선택")
file_frame.grid(row=0, column=4, padx=5, pady=5, sticky=N+E+W+S)

btn_add_file = Button(file_frame, padx=5, pady=5, width=12, text="파일추가", command=add_file)
btn_add_file.pack(side="left")

btn_del_file = Button(file_frame, padx=5, pady=5, width=12, text="선택삭제", command=del_file)
btn_del_file.pack(side="right")

# 리스트 프레임
list_frame = Frame(root)
list_frame.grid(row=1, column=4, padx=5, pady=5, sticky=E+W)

scrollbar = Scrollbar(list_frame)
scrollbar.pack(side="right", fill="y")

list_file = Listbox(list_frame, selectmode="extended", height=15, yscrollcommand=scrollbar.set)
list_file.pack(side="left", fill="both", expand=True)
scrollbar.config(command=list_file.yview)

# 진행 상황 Progress Bar
frame_progress = LabelFrame(root, text="진행상황")
frame_progress.grid(row=2, column=4, padx=5, pady=5, sticky=E+W)

p_var = DoubleVar()
progress_bar = ttk.Progressbar(frame_progress, maximum=100, variable=p_var)
progress_bar.pack(fill="x", padx=5, pady=5)



# 실행 프레임
frame_run = Frame(root)
frame_run.grid(row=3, column=4, sticky=N+E+W+S)

btn_close = Button(frame_run, padx=5, pady=5, text="닫기", width=12, command=root.quit)
btn_close.pack(side="right", padx=5, pady=5)

btn_start = Button(frame_run, padx=5, pady=5, text="시작", width=12, command=start_2)
btn_start.pack(side="right", padx=5, pady=5)


root.resizable(True, False) # x(너비), y(높이) 값 변경 불가 (창 크기 변경 불가)
root.mainloop()