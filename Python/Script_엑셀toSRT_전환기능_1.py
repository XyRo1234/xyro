from tkinter import * # __all__
from tkinter import filedialog
import tkinter as tk
from tkinter import PhotoImage, Button, Label, StringVar, ttk, colorchooser
import tkinter.ttk as ttk
import tkinter.messagebox as msgbox
import os
import pandas as pd
from pyairtable import Table
import re
import numpy
from chardet import detect
'''
Airtable 등에서 다운로드받은 Excel파일을 import하여 srt와 ssml파일을 생성해냄
단 One Excel파일에 E01,E02,....가 있어도 구분하여 각 에피소드별로 srt,ssml파일들을 뽑아냄
'''

root = Tk()
root.title("Airtable Excel Transform")
#root.geometry("640x480+300+100") # 가로 * 세로 + x좌표 + y좌표



# 파일 추가
def add_file():
    file = filedialog.askopenfilename(title="이미지 파일을 선택하세요", \
        filetypes=(("엑셀 파일", "*.csv *.xlsx"), ("모든 파일", "*.*")), \
        initialdir=r"D:\Program Files\Workspace\airtable")
        # 최초에 사용자가 지정한 경로를 보여줌
    if file == '': # 사용자가 취소를 누를 때
        return
    txt_add_file.delete(0, END)
    txt_add_file.insert(0, file)    


# 저장 경로 (폴더)
def browse_dest_path():
    folder_selected = filedialog.askdirectory()
    if folder_selected == '': # 사용자가 취소를 누를 때
        return
    #print(folder_selected)
    txt_dest_path.delete(0, END)
    txt_dest_path.insert(0, folder_selected)

def start_1():
    excelfile = txt_add_file.get()
    path = txt_dest_path.get()

    # 파일불러오기 / dataframe만들기

    if '.csv' in excelfile:
        try:
            df = pd.read_csv(f'{excelfile}', encoding='CP949',  na_values=["?", "??", "N/A", ""], keep_default_na= False)  # 엑셀값 dataframe만들기
        except UnicodeDecodeError:
            df = pd.read_csv(f'{excelfile}', encoding='utf-8',  na_values=["?", "??", "N/A", ""], keep_default_na= False)  # 엑셀값 dataframe만들기
    else:
        df = pd.read_excel(f'{excelfile}')

    header = df.columns.values.tolist()     # BOM값으로 인해 첫열 이름이 이상하게 변형되었을때, 열이름 변경하기
    if '癤풬o' in header:                   # BOM값으로 인해 첫열 이름이 이상하게 변형되었을때, 열이름 변경하기
        df.rename(columns={'癤풬o':'No'}, inplace=True) # 열이름 변경하기

    df = df.filter(items=['No','Episode','SRT_Time_Code','SRT/SSML'])     # df필요한 열만 추출

    df_ep_list_draft = df['Episode'].values.tolist()    # Episode 리스트 만들기 ( [E01,E01,E02,E02,E02,E03,...] )
    df_ep_list = []                             # Episode 리스트 중복값 제거
    for i,value in enumerate(df_ep_list_draft): # Episode 리스트 중복값 제거
        if value not in df_ep_list:             # Episode 리스트 중복값 제거
            df_ep_list.append(value)            # Episode 리스트 중복값 제거
    df_ep_list.sort
    # print(df_ep_list)

    for i,value in enumerate(df_ep_list):           # Episode별 순차진행
        df_ep = df.loc[(df['Episode'] == value)]    # Episode별 순차진행/특정Ep의 df만 남기기
        # print(df_ep)
        # 파일생성 및 data 입력
        with open(f'{path}\\(SRT){value}.srt', 'w', encoding='utf8') as fl:   # 파일 생성
            for i in range(0,df_ep.shape[0]):      # df.shape = [행수,열수] / 따라서 행수만큼 반복
                fl.write('\n')
                fl.write(str(i+1))
                fl.write('\n')
                fl.write(str(df_ep.loc[(df_ep['No']==i+1)]['SRT_Time_Code'].values[0]).strip())
                fl.write('\n')
                fl.write(str(df_ep.loc[(df_ep['No']==i+1)]['SRT/SSML'].values[0]).strip())
                # print(str(df_ep.loc[(df_ep['No']==i+1)]['SRT/SSML'].values[0]).strip())
                fl.write('\n')    

        with open(f'{path}\\(SSML){value}.txt', 'w', encoding='utf8') as fl:   # 파일 생성
            for i in range(0,df_ep.shape[0]):      # df.shape = [행수,열수] / 따라서 행수만큼 반복
                fl.write(str(df_ep.loc[(df_ep['No']==i+1)]['SRT/SSML'].values[0]).strip())
                # print(str(df_ep.loc[(df_ep['No']==i+1)]['SRT/SSML'].values[0]).strip())
                fl.write('\n')

        print(value,'완료')

        progress = (i + 1) / len(df_ep_list) * 100 # 실제 percent 정보를 계산
        p_var.set(progress)


# Column = 0 사이즈 조절
column_frame = Label(root, text="", width=60, height=0)
column_frame.grid(row=0, column=0)

# Import File 경로 프레임                                                                              # 왼쪽 첫번째
path_frame = LabelFrame(root, text="엑셀선택")
path_frame.grid(row=2, column=0, padx=5, pady=5, sticky=N+E+W+S)


txt_add_file = Entry(path_frame)
txt_add_file.pack(side="left", fill="x", expand=True, padx=5, pady=5, ipady=4) # 높이 변경

btn_add_file = Button(path_frame, text="찾아보기", width=10, command=add_file)
btn_add_file.pack(side="right", padx=5, pady=5)


# 저장 경로 프레임                                                                              # 왼쪽 첫번째
path_frame = LabelFrame(root, text="저장경로")
path_frame.grid(row=3, column=0, padx=5, pady=5, sticky=N+E+W+S)


txt_dest_path = Entry(path_frame)
txt_dest_path.pack(side="left", fill="x", expand=True, padx=5, pady=5, ipady=4) # 높이 변경

btn_dest_path = Button(path_frame, text="찾아보기", width=10, command=browse_dest_path)
btn_dest_path.pack(side="right", padx=5, pady=5)



# 진행 상황 Progress Bar
frame_progress = LabelFrame(root, text="진행상황")
frame_progress.grid(row=4, column=0, padx=5, pady=20, sticky=E+W)

p_var = DoubleVar()
progress_bar = ttk.Progressbar(frame_progress, maximum=100, variable=p_var)
progress_bar.pack(fill="x", padx=5, pady=5)


# 실행 프레임                                                                                   # 왼쪽 세번째
frame_run = Frame(root)
frame_run.grid(row=5, column=0)

btn_close = Button(frame_run, padx=5, pady=5, text="닫기", width=12, command=root.quit)
btn_close.pack(side="right", padx=5, pady=5)

btn_start = Button(frame_run, padx=5, pady=5, text="시작", width=12, command=start_1)
btn_start.pack(side="right", padx=5, pady=5)

# Column = 0 하단여백
column_frame = Label(root, text="", width=0, height=0)
column_frame.grid(row=100, column=0)


root.resizable(True, False) # x(너비), y(높이) 값 변경 불가 (창 크기 변경 불가)
root.mainloop()