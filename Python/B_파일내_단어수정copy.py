# encoding='UTF8'
# encoding='euc-kr'
# encoding='UTF-8-SIG'
from chardet import detect
import os
# for A in B : B의 index들을 꺼내서 A에 넣은 후, 실행. 리스트 끝까지.

def replace():
    ## 폴더내의 파일명을 리스트로 만들기
    path = "D:\\Program Files\\Workspace\\00_Default\\"
    path2 = "D:\\Program Files\\Workspace\\00_Create\\"
    draft_filenames = os.listdir(path)

    filenames = []
    for i in draft_filenames:
        if '.srt' in i:              # 'txt' or 'srt'가 포함되어있는 리스트 골라내기
            filenames.append(i)
    for i in draft_filenames:
        if '.txt' in i:
            filenames.append(i)
    for i in draft_filenames:
        if '.xml' in i:
            filenames.append(i)

    ## 인코딩방식 체크
    def get_encoding_type(filepath):
        with open(filepath, "rb") as file:
            rawdata = file.read()
            return detect(rawdata)['encoding']
        return None

    ## 파일내 단어수정
    for filename in filenames:
        # print(TXTSSML)

        src=[]
        tar=[]
        src.append("’")         # 기존내용      (right single quotation mark)
        tar.append("'")         # 바꾸려는 내용 (apostrophe)
        src.append("‘")         # 기존내용      (left single quotation mark)
        tar.append("'")         # 바꾸려는 내용 (apostrophe)
        src.append(" ")         # 기존내용      (NBSP)
        tar.append(" ")         # 바꾸려는 내용 (space)

        src.append("Self Care button")              # 기존내용
        tar.append("[Self Care] button")            # 바꾸려는 내용
        src.append("Lock button")                   # 기존내용
        tar.append("[Lock] button")                 # 바꾸려는 내용
        src.append("Craft Ice button")              # 기존내용
        tar.append("[Craft Ice] button")            # 바꾸려는 내용
        src.append("Ice On/Off button")             # 기존내용
        tar.append("[Ice On/Off] button")           # 바꾸려는 내용
        src.append("Ice Plus button")               # 기존내용
        tar.append("[Ice Plus] button")             # 바꾸려는 내용
        src.append("Express Freeze button")         # 기존내용
        tar.append("[Express Freeze] button")       # 바꾸려는 내용
        src.append("Water Filter button")           # 기존내용
        tar.append("[Water Filter] button")         # 바꾸려는 내용


        filepath = (f'{path}{filename}')
        filepath2 = (f'{path2}{filename}')
        read_codec = get_encoding_type(filepath)



        if read_codec == "ISO-8859-1":
            with open(filepath, "r", encoding='ISO-8859-1') as file:           # r : read
                content = file.read()
                i=0
                while i<=100:
                    try:
                        content = content.replace(src[i], tar[i])
                        i+=1
                    except  IndexError:
                        break
            with open(filepath2, "a", encoding='UTF-8-SIG') as file:           # w : write / a : append
                file.write(content)

        elif read_codec == "UTF-8-SIG":
            with open(filepath, "r", encoding='utf-8') as file:           # r : read
                content = file.read()
                i=0
                while i<=100:
                    try:
                        content = content.replace(src[i], tar[i])
                        i+=1
                    except  IndexError:
                        break
            with open(filepath2, "a", encoding='UTF-8') as file:           # w : write / a : append
                file.write(content)

        else:    
            with open(filepath, "r", encoding='utf-8') as file:           # r : read
                content = file.read()
                i=0
                while i<=100:
                    try:
                        content = content.replace(src[i], tar[i])
                        i+=1
                    except  IndexError:
                        break
            with open(filepath2, "a", encoding='UTF-8-SIG') as file:           # w : write / a : append
                file.write(content)

replace()
