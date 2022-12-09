# encoding='UTF8'
# encoding='euc-kr'
# encoding='UTF-8-SIG'
from chardet import detect
import os
# for A in B : B의 index들을 꺼내서 A에 넣은 후, 실행. 리스트 끝까지.

## 폴더내의 파일명을 리스트로 만들기
path = "D:\\Program Files\\Workspace\\00_Default\\"
path2 = "D:\\Program Files\\Workspace\\00_Create\\"
filenames = os.listdir(path)

## 인코딩방식 체크
def get_encoding_type(filepath):
    with open(filepath, "rb") as file:
        rawdata = file.read()
        return detect(rawdata)['encoding']
    return None

## 파일내 단어수정
for filename in filenames:
    # print(TXTSSML)
    src1 = "’"                                          # 기존내용      (right single quotation mark)
    tar1 = "'"                                          # 바꾸려는 내용 (apostrophe)
    src2 = "‘"                                          # 기존내용      (left single quotation mark)
    tar2 = "'"                                          # 바꾸려는 내용 (apostrophe)
    src3 = " "                                          # 기존내용      (NBSP)
    tar3 = " "                                          # 바꾸려는 내용 (space)

    filepath = (f'{path}{filename}')
    filepath2 = (f'{path2}{filename}')
    read_codec = get_encoding_type(filepath)

    if read_codec == "ISO-8859-1":
        with open(filepath, "r", encoding='ISO-8859-1') as file:           # r : read
            content = file.read()
            content = content.replace(src1, tar1)
            content = content.replace(src2, tar2)
            content = content.replace(src3, tar3)
        with open(filepath2, "a", encoding='UTF-8-SIG') as file:           # w : write / a : append
            file.write(content)

    else:    
        with open(filepath, "r", encoding='utf-8') as file:           # r : read
            content = file.read()
            content = content.replace(src1, tar1)
            content = content.replace(src2, tar2)
            content = content.replace(src3, tar3)
        with open(filepath2, "a", encoding='UTF-8-SIG') as file:           # w : write / a : append
            file.write(content)

