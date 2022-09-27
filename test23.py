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
import csv



def start_1():
    excelfile ='D:\\Program Files\\Workspace\\airtable\\aaa.xlsx'
    path = 'D:\\Program Files\\Workspace\\airtable'

    # 파일불러오기 / dataframe만들기
    if '.csv' in excelfile:
        try:
            df = pd.read_csv(f'{excelfile}', encoding='CP949',  na_values=["?", "??", "N/A", ""], keep_default_na= False)  # 엑셀값 dataframe만들기
        except UnicodeDecodeError:
            df = pd.read_csv(f'{excelfile}', encoding='utf-8',  na_values=["?", "??", "N/A", ""], keep_default_na= False)  # 엑셀값 dataframe만들기
    else:
        df = pd.read_excel(f'{excelfile}')


    print(df)




#     header = df.columns.values.tolist()     # BOM값으로 인해 첫열 이름이 이상하게 변형되었을때, 열이름 변경하기
#     if '癤풬o' in header:                   # BOM값으로 인해 첫열 이름이 이상하게 변형되었을때, 열이름 변경하기
#         df.rename(columns={'癤풬o':'No'}, inplace=True) # 열이름 변경하기

#     df = df.filter(items=['No','Episode','SRT_Time_Code','SRT/SSML'])     # df필요한 열만 추출
#     print(df)
#     df_ep_list_draft = df['Episode'].values.tolist()    # Episode 리스트 만들기 ( [E01,E01,E02,E02,E02,E03,...] )
#     print(df.apply)
#     df_ep_list = []                             # Episode 리스트 중복값 제거
#     for i,value in enumerate(df_ep_list_draft): # Episode 리스트 중복값 제거
#         if value not in df_ep_list:             # Episode 리스트 중복값 제거
#             df_ep_list.append(value)            # Episode 리스트 중복값 제거
#     df_ep_list.sort
#     # print(df_ep_list)

#     for i,value in enumerate(df_ep_list):           # Episode별 순차진행
#         df_ep = df.loc[(df['Episode'] == value)]    # Episode별 순차진행/특정Ep의 df만 남기기
#         print(df_ep)
#         # 파일생성 및 data 입력
#         with open(f'{path}\\{value}_create.srt', 'w', encoding='utf8') as fl:   # 파일 생성
#             for i in range(0,df_ep.shape[0]):      # df.shape = [행수,열수] / 따라서 행수만큼 반복
#                 fl.write('\n')
#                 fl.write(str(i+1))
#                 fl.write('\n')
#                 fl.write(str(df_ep.loc[(df_ep['No']==i+1)]['SRT_Time_Code'].values[0]).strip())
#                 fl.write('\n')
#                 fl.write(str(df_ep.loc[(df_ep['No']==i+1)]['SRT/SSML'].values[0]).strip())
#                 # print(str(df_ep.loc[(df_ep['No']==i+1)]['SRT/SSML'].values[0]).strip())
#                 fl.write('\n')

start_1()