# pip install requests
# pip install beautifulsoup4
# pip install lxml
# pip install selenium
# https://www.selenium.dev/downloads/

import time
import pandas as pd
import requests
from bs4 import BeautifulSoup
from selenium import webdriver

# Url = "http://gmds.lge.com/lgcms/topics"
# headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko"}
# res = requests.get(Url, headers=headers)
# res.raise_for_status()                                  # Url을 불러오는데 문제가 있으면, 중지시켜줌
# # with open("test3.html", "w", encoding="utf8") as f:   # 불러온 사이트 html을 파일로 저장
# #     f.write(res.text)
# soup = BeautifulSoup(res.text,"lxml")   # html문서값을 lxml파서를 통해서 soup객체로 만듬.
# # print(soup.find_all("a"))

url = 'http://gmds.lge.com/lgcms/topics'
browser = webdriver.Ie('./IEDriverServer.exe')
browser.get(url)
browser.set_window_position(0,0)
browser.set_window_size(1020,1080)
browser.find_element_by_id("username").send_keys("edward.kwon")
time.sleep(10)
# browser.find_element_by_id("password").send_keys("비밀번호 입력")
browser.find_element_by_class_name("login-button").click()
time.sleep(1)

path = "D:\\Program Files\\Workspace\\others\\GMDS\\"
GMDS_info_file = 'GMDS_Topic_WM_US.xlsx'
df_excel = pd.read_excel(f'{path}{GMDS_info_file}', index_col=None)

# US_titles = ['How to Use the Ice and Water Dispenser', 'How to Use the Ice Maker', 'How to Clean the Inside of the Refrigerator', 'How to Clean the Air Filter', 'How to Change the Water Filter (located inside the refrigerator)', 'Refrigerator_Not_Cooling', 'In Door Ice Maker Not Working', 'Craft Ice Maker Not Working', 'Water Is Not Dispensing', 'Water Tastes Bad', 'Refrigerator Door Not Closing', 'How to Find My Refrigerator Model Number', 'Choosing the Proper Installation Location', 'How to Remove and Assemble the Refrigerator Door', 'How_to_Connect_the_Water_Line', 'How to Align the Refrigerator Door', 'How to Level the Refrigerator']
i = 0
titles = []
while i<100:
    try:
        GMDS_title = str(df_excel.loc[i,'title'])
        titles.append(GMDS_title)
        i= i+1
    except KeyError:
        break
print(titles)

Topic_No_list = []
Topic_Title_list = []
Region_list = []
for title in titles:
    time.sleep(1)
    browser.find_element_by_xpath('/html/body/div[2]/div[2]/div[2]/button').click() # Create topic 클릭
    browser.find_element_by_xpath('//*[@id="title"]').send_keys(title)                                               # title 입력
    browser.find_element_by_xpath('/html/body/div[9]/div[2]/form/div[3]/div[1]/div/select/option[2]').click()           # Not Belong 클릭
    browser.find_element_by_xpath('//*[@id="product-id"]/option[35]').click()                                           # Product(*) : VideoGuidance 클릭
    time.sleep(0.5)
    browser.find_element_by_xpath('/html/body/div[9]/div[2]/form/div[5]/div[2]/div/select/optgroup/option[1]').click()  # Platform : Front Loader / SxS 
    time.sleep(0.5)
    # browser.find_element_by_xpath('/html/body/div[9]/div[2]/form/div[6]/div[1]/div/select/optgroup/option[1]').click()  # Region : GLOBAL
    browser.find_element_by_xpath('/html/body/div[9]/div[2]/form/div[6]/div[1]/div/select/optgroup/option[2]').click()  # Region : NORTH AMERICA
    browser.find_element_by_xpath('/html/body/div[9]/div[2]/form/div[7]/div[1]/div/select/option[2]').click()           # Category : CC
    browser.find_element_by_xpath('/html/body/div[9]/div[2]/form/div[9]/button[3]').click()                             # Create 클릭
    time.sleep(2)
    Topic_No = browser.find_elements_by_class_name('topic-index-topic-info-open')[0].text       # Topic_No 정보가져오기
    Topic_No_list.append(Topic_No)
    Topic_Title = browser.find_elements_by_class_name('topic-index-topic-info-open')[2].text    # Topic_Title 정보가져오기
    Topic_Title_list.append(Topic_Title)
    Region = browser.find_elements_by_class_name('topic-index-topic-info-open')[6].text         # Region 정보가져오기
    Region_list.append(Region)

    Data = [Topic_No_list,Topic_Title_list,Region_list]
    df = pd.DataFrame.from_records(Data)
    df = df.transpose()
    print(df.head())


# print(Topic_No_list)
# print(Topic_Title_list)
# print(Region_list)

""" DataFrame 만들기 (Topic_No / Topic_Title / Region) """
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
GMDS_info_file = 'GMDS_Topic_Info.csv'                           # 엑셀파일명 지정
df.to_csv(f'{path}{GMDS_info_file}', header = True, index = True)   # 엑셀파일 만들기