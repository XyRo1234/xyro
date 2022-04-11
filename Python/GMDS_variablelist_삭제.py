import os
from selenium import webdriver
import time
import pandas as pd
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import pyautogui
import re

browser = webdriver.Ie('./IEDriverServer.exe')
actionChains = ActionChains(browser)
url = 'http://gmds.lge.com/lgcms/topics/'
browser.get(url)
# browser.set_window_position(0,0)
# browser.set_window_size(1020,600)
browser.find_element_by_id("username").send_keys("ws.jung")
browser.find_element_by_class_name("login-button").click()


path = "D:\\Program Files\\Workspace\\others\GMDS\\"           # 엑셀파일 경로
GMDS_info_file = 'GMDS_Topic_UK.xlsx'                           # 엑셀파일 명
df = pd.read_excel(f'{path}{GMDS_info_file}', index_col=None)   # 엑셀 DataFrame 가져오기

i=0
while i<1000:
    try:
        lines = []
        No = int(df.loc[i,'No'])
        print(df.loc[i,'title'])
        i= i+1

        url = f'http://gmds.lge.com/lgcms/Editor/src/topic?num=000{No}&r=1'
        browser.get(url)
        # browser.set_window_size(1020,600)
        time.sleep(2)

        browser.find_element_by_id('treeToggle').click()
        time.sleep(1)

        p = re.compile("t_\d*_r1_\d*_\d*")
        get_id = browser.find_elements_by_class_name('pos1')[0].get_attribute('id')
        m = p.match(get_id)
        print(m.group())
        browser.find_element_by_id(f'{m.group()}_tree_icon').click() # 닫혀있는 tree의 (+) 누르기
        time.sleep(0.5)

        variablelist_qty = browser.find_elements_by_xpath("//*[text()='variablelist']")
        for qty in variablelist_qty:
            target = browser.find_elements_by_class_name('pos1')[2]     # variablelist
            actionChains.context_click(target).perform()    # 우클릭
            browser.find_element_by_xpath('/html/body/div[30]/div[1]/div[7]').click()   # Delete 0-5
            time.sleep(0.5)
            alert = browser.switch_to.alert
            alert.accept()
            
        """ Save """
        browser.find_element_by_id('f').click()                     # File 탭 클릭
        browser.find_element_by_id('_mulcome_obj_0-1').click()      # Save 클릭
        time.sleep(2)

    except KeyError:
        print("마지막 Topic 넘버를 불러왔었기에 종료합니다.")
        break
    except ValueError:
        print("마지막 Topic 넘버를 불러왔었기에 종료합니다.")
        break