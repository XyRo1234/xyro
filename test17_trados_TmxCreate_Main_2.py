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



#file_fullname = r"D:\test\ru-RU_test.tmx"



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
    for file in list_file.get(0, END):
        print(file)
        p = re.compile("..-[a-zA-Z]{2}")    # re.compile('..-[a-zA-Z]{2}')
        m = p.search(file)         # <re.Match object; span=(0, 5), match='ar-AE'>
        lang2 = m.group()                  # ar-AE
        print(lang2)
        start_1(file,lang2)


def start_1(file_fullname, lang2):
    filename=os.path.basename(file_fullname)
    file_path = os.path.dirname(file_fullname)

    lang1 = 'en-GB'
    # lang2 = 'ru-RU'


    def sentence_cut(content):
        m = re.findall("..\. ", content)
        n = re.split("..\. ", content)
        for index,value in enumerate(n):
            try:
                n.insert(index,(value+m[index]).strip())
                n.remove(n[index+1])
            except IndexError:
                break
        return list(n)

    # <tu  ~  </tu> : '(?<=\<tu)(.*?)(?=<\/tu>)'
    # "(?<=\<seg>)(.*?)(?=<\/seg>)"

    # def extract_string(target):
    #     return re.sub('<[^>]*>','',target)


    with open(file_fullname, "r", encoding='utf-8') as file:           # r : read
            content = str(file.read())
            content = content.replace('\n',' ')
            # w = ''
            # for a in content:
            #     print(w)
            #     w = w + " " + str(a)

            p = re.compile("(?<=\<seg>)(.*?)(?=<\/seg>)")    # re.compile('..-[a-zA-Z]{2}')
            m = p.findall(content)                  # <re.Match object; span=(0, 5), match='ar-AE'>
            # print(m)

            en = []
            ru = []
            en_execpt = []
            ru_execpt = []

            for index, value in enumerate(m):
                    if(index%2==0):
                        # print(index,"짝수입니다.")
                        en_list = sentence_cut(value)                    
                        en_len = len(en_list)
                        # print(index,"짝수입니다.")
                    else:
                        # print("홀수입니다.")
                        ru_list = sentence_cut(value)
                        ru_len = len(ru_list)
                        if en_len == ru_len:
                            for en_val in en_list:
                                en.append(en_val)
                            for ru_val in ru_list:
                                ru.append(ru_val)
                        else:                           # 예외항목 별도 저장
                            w=''
                            q=''
                            for i in en_list: w = w +' '+ i
                            en_execpt.append(w)
                            en_list
                            for i in ru_list: q = q +' '+ i
                            ru_execpt.append(q)

            # print(en)
            # print(ru)
            print(len(en))  # ru 총 segment
            print(len(ru))  # ru 총 segment


    with open(f'{file_path}\\New_{lang2}.tmx', "w", encoding='utf-8') as file:
        file.write(f'<?xml version="1.0" encoding="utf-8"?><tmx version="1.4"><header creationtool="SDL Language Platform" creationtoolversion="8.1" o-tmf="SDL TM8 Format" datatype="xml" segtype="sentence" adminlang="{lang1}" srclang="{lang1}" creationdate="20180711T065553Z" creationid="trados2015-PC\trados2015"><prop type="x-Comment:MultipleString"></prop><prop type="x-Recognizers">RecognizeNumbers, RecognizeAcronyms, RecognizeVariables, RecognizeMeasurements, RecognizeAlphaNumeric</prop><prop type="x-IncludesContextContent">True</prop><prop type="x-TMName">{lang2}</prop><prop type="x-TokenizerFlags">DefaultFlags</prop><prop type="x-WordCountFlags">DefaultFlags</prop></header><body>')
        file.write('\n')

        for index,value in enumerate(en):
            file.write(f'<tu creationdate="20220415T{100001+index}Z" creationid="LGE\ws.jung" changedate="20220415T{100001+index}Z" changeid="LGE\ws.jung" lastusagedate="20220415T{100001+index}Z">')
            file.write('\n')
            file.write('  <prop type="x-LastUsedBy">LGE\ws.jung</prop>')
            file.write('\n')
            file.write('  <prop type="x-Context">0, 0</prop>')
            file.write('\n')
            file.write('  <prop type="x-Origin">TM</prop>')
            file.write('\n')
            file.write('  <prop type="x-ConfirmationLevel">Translated</prop>')
            file.write('\n')
            file.write(f'  <tuv xml:lang="{lang1}">')
            file.write('\n')
            file.write(f'    <seg>{en[index]}</seg>')
            file.write('\n')
            file.write('  </tuv>')
            file.write('\n')
            file.write(f'  <tuv xml:lang="{lang2}">')
            file.write('\n')
            file.write(f'    <seg>{ru[index]}</seg>')
            file.write('\n')
            file.write('  </tuv>')
            file.write('\n')
            file.write('</tu>')
            file.write('\n')

        for index,value in enumerate(en_execpt):    # 예외항목 저장
            file.write(f'<tu creationdate="20220415T{100001+index}Z" creationid="LGE\ws.jung" changedate="20220415T{100001+index}Z" changeid="LGE\ws.jung" lastusagedate="20220415T{100001+index}Z">')
            file.write('\n')
            file.write('  <prop type="x-LastUsedBy">LGE\ws.jung</prop>')
            file.write('\n')
            file.write('  <prop type="x-Context">0, 0</prop>')
            file.write('\n')
            file.write('  <prop type="x-Origin">TM</prop>')
            file.write('\n')
            file.write('  <prop type="x-ConfirmationLevel">Translated</prop>')
            file.write('\n')
            file.write(f'  <tuv xml:lang="{lang1}">')
            file.write('\n')
            file.write(f'    <seg>{en_execpt[index]}</seg>')
            file.write('\n')
            file.write('  </tuv>')
            file.write('\n')
            file.write(f'  <tuv xml:lang="{lang2}">')
            file.write('\n')
            file.write(f'    <seg>{ru_execpt[index]}</seg>')
            file.write('\n')
            file.write('  </tuv>')
            file.write('\n')
            file.write('</tu>')
            file.write('\n')

        file.write('  </body>')
        file.write('\n')
        file.write('</tmx>')


    # print(f'예외항목 : {en_execpt}')

    with open(f'{file_path}\\{filename}.txt', "w", encoding='utf-8') as file:
        for index,i in enumerate(en_execpt):
            file.write('\n')
            if index==0: file.write(str(len(en_execpt)))
            file.write(str(index+1)+'\n')
            file.write(i)
        file.write('\n')    # en, ru구분을 위한 줄바꿈
        file.write('\n')    #
        file.write('\n')    #
        for index,i in enumerate(ru_execpt):
            file.write('\n')
            if index==0: file.write(str(len(ru_execpt)))
            file.write(str(index+1)+'\n')
            file.write(i)



# 파일 프레임 (파일 추가, 선택 삭제)                                                   
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
