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

innerTreeView = 't_00068783_r1_20220113112838_1_tree_icon'
p = re.compile("t_\d*_r1_\d*_\d*")
print(p.search(innerTreeView))
m = p.match(innerTreeView)
print(m.group()+'tree_icon')


""" HTML 뽑기 """
html = browser.find_element_by_xpath('//*').get_attribute('outerHTML')
# print(html)
with open('D:\\Program Files\\Workspace\html.txt', "w", encoding='UTF-8-SIG') as file:           # w : write / a : append
    file.write(html)


""" 정규표현식으로 id 찾기 """
p = re.compile("t_\d*_r1_\d*_\d*")
get_id = browser.find_elements_by_class_name('pos1')[0].get_attribute('id')
m = p.match(get_id)
print(m.group())
browser.find_element_by_id(f'{m.group()}_tree_icon').click() # 닫혀있는 tree의 (+) 누르기


""" 경로 예시 """
# //*[@id="main_pack"]/section[1]/div/div[2]
""" find_element 사용법 """
variablelist_qty = browser.find_elements_by_xpath("//*[text()='variablelist']")     # 해당 Text 수량 파악
browser.find_elements_by_class_name('item')[0].click()



""" 팝업 알람 클릭 """
alert = browser.switch_to.alert
alert.accept()


