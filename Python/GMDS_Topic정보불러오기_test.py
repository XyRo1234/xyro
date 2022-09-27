# import re
# lines = ['How to use dispenser', '- EzEz - - ', 'press - [Craft Ice] button' ,'hello world' ]

# p = re.compile("^How to ")
# p2 = re.compile("^-")
# i=0

# for l in lines:
#     m = p.match(l)
#     m2 = p2.match(l)
#     l = l.strip()
#     if m or m2:
#         try:
#             # print(m.group())
#             print(m2.group())
#             l = re.sub(p2, '뀨', l)
#             print(l)
#             print(i, '성공?')
#             i= i+1
#         except :
#             print(i, '성공?')
#             i= i+1

#     else:
#         print(i, '조건X')
#         i= i+1


from cgitb import text
import time
import pandas as pd
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from collections import OrderedDict

browser = webdriver.Ie('./IEDriverServer.exe')
browser.get('http://gmds.lge.com/lgcms/topics')
browser.find_element_by_id("username").send_keys("ws.jung")
browser.find_element_by_class_name("login-button").click()
time.sleep(1)

Topic_No_list = []
Topic_Title_list = []
Region_list = []

Topic_No = browser.find_elements_by_class_name('topic-index-topic-info-open')[0].text
Topic_No_list.append(Topic_No)
Topic_Title = browser.find_elements_by_class_name('topic-index-topic-info-open')[2].text
Topic_Title_list.append(Topic_Title)
Region = browser.find_elements_by_class_name('topic-index-topic-info-open')[6].text
Region_list.append(Region)

Topic_No = browser.find_elements_by_class_name('topic-index-topic-info-open')[10].text
Topic_No_list.append(Topic_No)
Topic_Title = browser.find_elements_by_class_name('topic-index-topic-info-open')[12].text
Topic_Title_list.append(Topic_Title)
Region = browser.find_elements_by_class_name('topic-index-topic-info-open')[16].text
Region_list.append(Region)

print(Topic_No_list)
print(Topic_Title_list)
print(Region_list)


First_Data = [{'No':Topic_No_list[0], 'Topic Title':Topic_Title_list[0],'Region':Region_list[0]}]
df = pd.DataFrame(First_Data)
i=1
while i < 100:
    try:
        df.loc[i]=[Topic_No_list[i], Topic_Title_list[i],Region_list[i]]
        i+=1
    except:
        break
print(df)


path = "D:\\Program Files\\Workspace\\others\\GMDS\\"           # 엑셀파일 경로 지정
GMDS_info_file = 'GMDS_Topic_Info_test.csv'                           # 엑셀파일명 지정
df.to_csv(f'{path}{GMDS_info_file}', header = True, index = True)   # 엑셀파일 만들기

time.sleep(1)