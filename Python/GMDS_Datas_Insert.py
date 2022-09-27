import os
from selenium import webdriver
import time
import pandas as pd
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import pyautogui
import re

# """ line 리스트 만들기 """

# path2 = "D:\\Program Files\\Workspace\\00_Create\\"
# filenames = os.listdir(path2)
# ## 파일명리스트(filename)에서 txt or srt파일 골라내기.
# srt_file = []                       # 골라낸 파일 리스트
# for i in filenames:
#     if '.srt' in i:              # 'txt' or 'srt'가 포함되어있는 리스트 골라내기
#         srt_file.append(i)
# ## 파일명리스트(filename)에서 txt or srt파일 골라내기.
# txt_file = []                       # 골라낸 파일 리스트
# for i in filenames:
#     if '.txt' in i:              # 'txt' or 'srt'가 포함되어있는 리스트 골라내기
#         txt_file.append(i)
# ## 파일명리스트(filename)에서 txt or srt파일 골라내기.
# xml_file = []                       # 골라낸 파일 리스트
# for i in filenames:
#     if '.xml' in i:              # 'txt' or 'srt'가 포함되어있는 리스트 골라내기
#         xml_file.append(i)

browser = webdriver.Ie('./IEDriverServer.exe')
url = f'http://gmds.lge.com/lgcms/topics'
browser.get(url)
browser.set_window_position(0,0)
browser.set_window_size(1020,600)
browser.find_element_by_id("username").send_keys("edward.kwon")
time.sleep(10)
# browser.find_element_by_id("password").send_keys("비밀번호 입력")
browser.find_element_by_class_name("login-button").click()

path = "D:\\Program Files\\Workspace\\others\\GMDS\\"           # 엑셀파일 경로
GMDS_info_file = 'GMDS_Topic_WM_US.xlsx'                           # 엑셀파일 명
df = pd.read_excel(f'{path}{GMDS_info_file}', index_col=None)   # 엑셀 DataFrame 가져오기

i=0
while i<1000:
    try:
        lines = []
        No = int(df.loc[i,'No'])
        # GMDS_episode = str(df.loc[i,'episode'])
        # GMDS_title = str(df.loc[i,'title'])
        GMDS_filename = str(df.loc[i,'filename'])               # 불러올 파일명(txt)
        path2 = "D:\\Program Files\\Workspace\\00_Create\\"     # 불러올 파일(txt) 경로
        print(f'{No}:{GMDS_filename.rjust(40)}')
        lines = []
        with open(f'{path2}{GMDS_filename}','r',encoding = 'utf8') as fr:
            data = fr.readlines()
            for l in data:
                if l != '':
                    lines.append(l)
        i= i+1

        """topic에 로그인 및 접속 """
        url = f'http://gmds.lge.com/lgcms/Editor/src/topic?num=000{No}&r=1'       
        # url = f'http://gmds.lge.com/lgcms/Editor/src/topic?num=00069178&r=1'          # test용 토픽
        browser.get(url)
        browser.set_window_size(1020,600)
        # browser.find_element_by_id("username").send_keys("ws.jung")
        # browser.find_element_by_class_name("login-button").click()
        time.sleep(2)

        """ Variablelist 추가 """
        browser.find_element_by_id('treeToggle').click()
        actionChains = ActionChains(browser)
        target = browser.find_element_by_xpath('/html/body/div[3]/div[3]/div[2]/div[1]/div[2]').click() # topic 선택
        actionChains.context_click(target).perform()    # 우클릭
        browser.find_element_by_xpath('/html/body/div[30]/div[1]/div[6]').click()   # Insert element 0-4
        browser.find_element_by_xpath('/html/body/div[30]/div[3]/div[3]').click()   # Insert to child 2-1
        browser.find_element_by_xpath('/html/body/div[30]/div[5]/div[4]').click()   # variablelist 4-3

        """ 마우스 이동 (x 좌표, y 좌표) """
        # position = pyautogui.position()
        # print(position.x)
        # print(position.y)
        pyautogui.moveTo(345,355)
        pyautogui.click()

        lines_modify = []
        for l in lines:
            l = l.strip()
            if l != '':
                lines_modify.append(l)

        p = re.compile("^-")
        for index, l in enumerate(lines_modify):
            l = l.strip()
            m = p.match(l)
            if m:
                # target = browser.find_element_by_xpath('/html/body/div[3]/div[3]/div[2]/div[1]/div[2]').click() # topic 선택
                target = browser.find_elements_by_class_name('item')[0].click() # topic 선택 (이상동작이 추가 발생해서 한번 더 선택코드 삽입)
                target = browser.find_elements_by_class_name('item')[0].click() # topic 선택 (위 이유로 한번 더 선택)                              
                actionChains.context_click(target).perform()    # 우클릭
                browser.find_element_by_xpath('/html/body/div[30]/div[1]/div[6]').click()   # Insert element 0-4
                browser.find_element_by_xpath('/html/body/div[30]/div[3]/div[3]').click()   # Insert to child 2-1
                browser.find_element_by_xpath('/html/body/div[30]/div[5]/div[4]').click()   # variablelist 4-3
                l = (re.sub(p,'', l)).strip()        # 첫 - 없애기
                actionChains.send_keys(l).perform()  # 소제목 타이핑
                # actionChains.send_keys(Keys.ENTER).perform()  # Enter 타이핑
                pyautogui.moveTo(345,475)
                pyautogui.click()           # Para 클릭 (클릭후 왼쪽 Structure View에서 구조이동이 발생하면서 클릭이 풀리는 현상이 발생함)
                time.sleep(1)               # 1초동안 구조이동시간 기다림
                pyautogui.moveTo(345,475)
                pyautogui.click()           # Para 재클릭 (구조이동이 완료된 후에 다시 클릭을 진행해줌)
            else:
                actionChains.send_keys(l).perform()  # line값 타이핑
                if len(lines_modify)-1 == index:                # 마지막 index일때, 엔터를 치지 않음
                    continue
                elif p.match(lines_modify[(index)+1]):          # 다음 index가 소제목(-)조건일 경우, 엔터를 치지 않음
                    continue
                else:
                    actionChains.send_keys(Keys.ENTER).perform()  # Enter 타이핑

        time.sleep(1)
        
        """ Save """
        browser.find_element_by_id('f').click()                     # File 탭 클릭
        browser.find_element_by_id('_mulcome_obj_0-1').click()      # Save 클릭
    
    except KeyError:
        print("마지막 Topic 넘버를 불러왔었기에 종료합니다.")
        break
    except ValueError:
        print("마지막 Topic 넘버를 불러왔었기에 종료합니다.")
        break