
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



base = 'appMARg1QXBRWvzrV'

i = r'D:\Program Files\Workspace\airtable\E05_How to Clean the Inside of the Refrigerator_원석수정.srt'
filename=os.path.basename(i)
path = os.path.dirname(i)

# 인코딩체크
def get_encoding_type(filepath):
    with open(filepath, "rb") as file:
        rawdata = file.read()
        return detect(rawdata)['encoding']
    return None

ep_list = []
number_list = []
time_list = []
srt_list = []
fields_id_list = []

check_unicode = get_encoding_type(f'{path}/{filename}')
p = re.compile("ISO-8859")                   # re.compile('..-[a-zA-Z]{2}')
m = p.search(check_unicode)                  # <re.Match object; span=(0, 5), match='ar-AE'>
if m:
    regular = m.group()                  # ar-AE
    print(regular)
    msgbox.showwarning("경고", f"{filename}의 인코딩타입이 {check_unicode}입니다. 인코딩타입을 변경해주세요.")

ep_number = re.compile("E\d{2}").search(filename).group()
with open(f'{path}/{filename}','r',encoding='utf-8') as fl:
    data = fl.readlines()
    for i,l in enumerate(data):
        line = l.strip()    # 양옆의 빈칸 삭제

        check = list(line)                                  # BOM코드 날리기
        try:                                                # BOM코드 날리기
            if str(check[0])=='\ufeff':                     # BOM코드 날리기
                print('BOM코드있음')                        # BOM코드 날리기
                del(check[0])                               # BOM코드 날리기
                create_line = ''                            # BOM코드 날리기
                for a in check:                             # BOM코드 날리기
                    create_line = create_line + str(a)      # BOM코드 날리기
                line = create_line                          # BOM코드 날리기
                # print(line)                                 # BOM코드 날리기
        except:                                             # BOM코드 날리기
            continue                                        # BOM코드 날리기

        if line.isdigit():  # 숫자만 있는 것인지 확인
            number_list.append(line)
            time_list.append(data[i+1].strip())
            try:
                srt_list.append(data[i+2].strip())
            except:
                pass
            ep_list.append(ep_number)

dic = {
    'Episode': ep_list,    
    'No': number_list,
    'SRT_Time_Code': time_list,
    'SRT/SSML': srt_list
}
df = pd.DataFrame.from_dict(dic, orient='index')
df = df.transpose()     # DataFrame 행열 전환

# file_name = filename.split('.')[0]
# df.to_csv(f'{path}/{file_name}.csv', encoding='utf-8-sig', header = True, index = False)   # 엑셀파일로 생성



api_key = os.environ["AIRTABLE_API_KEY"]
base_id = base
table_conti = Table(api_key, base_id, 'Conti')
draft_table_conti = table_conti.all(sort=["No"])

df_table_conti = pd.json_normalize(draft_table_conti)            # json형식의 DataFrame으로 변환
print(df_table_conti.columns.values.tolist())
if not "fields.SRT_Time_Code" in df_table_conti.columns.values.tolist(): df_table_conti["fields.SRT_Time_Code"] = ""    # df 열에 fields.SRT_Time_Code이 없으면 새로 생성(df에 없을때 오류남)
if not "fields.SRT/SSML" in df_table_conti.columns.values.tolist(): df_table_conti["fields.SRT/SSML"] = ""              # df 열에 fields.SRT/SSML이 없으면 새로 생성(df에 없을때 오류남)

for col in df_table_conti.columns:                   # 정규식을 이용해서, 정렬을 위한 column값(header) 네임 찾기
    if re.compile("Episode$").search(col):
        episode = col
    if re.compile("No$").search(col):
        no = col

# print('정렬순서1 : '+episode)
# print('정렬순서2 : '+no)
df_table_conti = df_table_conti.sort_values(by=[episode, no])     # 해당 column기준으로 정렬

type_no = type(df_table_conti.loc[[0],['fields.No']].iat[0,0])      # No열이 [# Number]이 아니면 에러가 뜸으로(str이라서),변경필요 체크.
if not type_no == numpy.int64:
    print(f'{type_no} No열의 타입을 [# Number]로 변경해주세요.')

df_table_conti_EP = df_table_conti.loc[(df_table_conti['fields.Episode'] == ep_number), ['id','fields.Episode','fields.No','fields.SRT_Time_Code', 'fields.SRT/SSML']] 
                                                                    # ep_number(E01, E02, ...)인 항목만 남기고, 위의 columns열만 추출해서 dataframe 생성
# print(df_table_conti_EP)

for i in range(0,df_table_conti_EP.shape[0]):# df.shape = [행수,열수] / 따라서 행수만큼 반복
    fields_id_list.append(str(df_table_conti_EP.loc[df_table_conti_EP['fields.No']==i+1, ['id']].iat[0,0]).strip())   # id값 찾기 및 id리스트만들기
    try:
        table_conti.update(fields_id_list[i], {'SRT_Time_Code':time_list[i]})
    except IndexError:
        print('Airtable과 SRT_Time_Code의 리스트수가 맞지않습니다. 확인해주세요.')
    try:
        table_conti.update(fields_id_list[i], {'SRT/SSML':srt_list[i]})
    except IndexError:
        print('Airtable과 SRT/SSML의 리스트수가 맞지않습니다. 확인해주세요.')
        
print(ep_number,'완료되었습니다.')