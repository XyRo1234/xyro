import requests
from bs4 import BeautifulSoup
import pandas as pd

url = 'https://www.lg.com/common/index.jsp'
res = requests.get(url)
# print("응답코드 :", res.status_code)    # 200이면 정상, 403이면 접근권한없음
res.raise_for_status()                 # 접속이 안되고 문제가 생기면, 여기서 프로그램을 끝낸다.

soup = BeautifulSoup(res.text, "lxml")    # Html정보를 lxml파서를 통해서 soup이란 객체로 만듬

countrys = {}
data = soup.find_all("a", attrs={"data-link-area":"select_your_region"})
for i in data:
    name_lang = i["data-link-name"]
    site = i["href"]
    if "http" in site:
        countrys[name_lang] = site
    else:
        countrys[name_lang] = f"https://www.lg.com{site}"

dic = {
    'country_language': countrys.keys(),
    'site': countrys.values(),
    }
df = pd.DataFrame.from_dict(dic, orient='index')
df = df.transpose()     # DataFrame 행열 전환
print(df)

Create_path = 'D:\\Program Files\\workspace\\00_Create\\'

df.to_excel(f'{Create_path}URL_list.xlsx', header = True, index = False)