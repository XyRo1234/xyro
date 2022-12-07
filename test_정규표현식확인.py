import os
from selenium import webdriver
import time
import pandas as pd
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import pyautogui
import re

# from lib2to3.pgen2 import driver
# from selenium import webdriver
# import selenium

# driver = webdriver.Chrome('./chromedriver.exe')
# # url = 'https://www.google.com'
# # driver.get(url)


# URL ="https://www.bing.com/search?q=site%3Alocalbitcoins.com&qs=n&sp=-1&pq=site%3Alocalbitcoins.com&sc=0-22&sk=&cvid=D38F613A00C64A88B2C0F87BD653088A&first=0"
# driver.get(URL)
# for link in driver.find_elements_by_css_selector("span"):
#     print(link.get_attribute('id'))




# import pandas as pd
# import os
# path2 = "D:\\Program Files\\Workspace\\00_Create\\"
# filenames = os.listdir(path2)
# ## 파일명리스트(filename)에서 txt or srt파일 골라내기.
# txt_file = []                       # 골라낸 파일 리스트
# for i in filenames:
#     if '.txt' in i:              # 'txt' or 'srt'가 포함되어있는 리스트 골라내기
#         txt_file.append(i)

# path = "D:\\Program Files\\Workspace\\others\\GMDS\\"
# filename = 'GMDS_Topic.xlsx'
# df = pd.read_excel(f'{path}{filename}', index_col=None)
# df['filename'] = txt_file
# print(df)



# l = "So when Should You Replace the Water Filter"
# p = re.compile("^How to ")
# p2 = re.compile("^So when")
# m = p.match('How to replace water filter')
# m2 = p2.match(l)


# print(m)
# print(m2)



# import pandas as pd
# import os
# path2 = "D:\\Program Files\\Workspace\\00_Create\\"
# filepath2 = "D:\\Program Files\\Workspace\\00_Create\\filenames.txt"
# filenames = os.listdir(path2)
# ## 파일명리스트(filename)에서 txt or srt파일 골라내기.
# txt_file = []                       # 골라낸 파일 리스트
# for i in filenames:
#     if '.txt' in i:              # 'txt' or 'srt'가 포함되어있는 리스트 골라내기
#         txt_file.append(i)
# for filename in txt_file:
#     with open(filepath2, "a", encoding='UTF-8-SIG') as file:
#         file.write(filename)
#         file.write('\n')


# innerTreeView = 't_00068783_r1_20220113112838_1_tree_icon'
# p = re.compile("t_\d*_r1_\d*_\d*")
# print(p.search(innerTreeView))
# m = p.match(innerTreeView)
# print(m.group()+'tree_icon')


file_name = 'New_(US_SRT)E01_How_to_Use_the_Ice_and_Water_Dispenser_211221.txt'
p = re.compile("E\d{2}")
print(p.search(file_name))  # <re.Match object; span=(12, 15), match='E01'>
m = p.search(file_name)       # <re.Match object; span=(12, 15), match='E01'>
m.group()                   # E01
print(m.group())            # E01




name = "ar-AE"

p = re.compile("..-[a-zA-Z]{2}")    # re.compile('..-[a-zA-Z]{2}')
m = p.search(name)                  # <re.Match object; span=(0, 5), match='ar-AE'>
wsname = m.group()                  # ar-AE

if p.match(name):
    print(p)
    print(m)
    print("매치됨  "+wsname)
else:
    print("매치안됨  "+wsname)

test = 'Craft Ice Maker Craft Ice is small'

p = re.compile(".+(?=Maker)")    # re.compile('..-[a-zA-Z]{2}')
m = p.search(test)                  # <re.Match object; span=(0, 5), match='ar-AE'>
wsname = m.group()                  # ar-AE
print(wsname)


# "(?<=\<seg>)(.*?)(?=<\/seg>)"

test = 'aSO-8859-1'

p = re.compile("ISO-8859")    # re.compile('..-[a-zA-Z]{2}')
m = p.search(test)                  # <re.Match object; span=(0, 5), match='ar-AE'>

if m:
    regular = m.group()                  # ar-AE
    print(regular)

# regular = m.group()                  # ar-AE
# regular = re.compile("ISO-8859").search(test).group()
# print(regular)


test2 = 'New_(UK_SSML)E13_Water_Is_Not_Dispensing_220321.ssml'

p = re.compile("_\d{4,}.ssml")    # re.compile('..-[a-zA-Z]{2}')
m = p.search(test2)                  # <re.Match object; span=(0, 5), match='ar-AE'>

if m:
    regular = m.group()                  # ar-AE
    print('test2')
    print(regular)