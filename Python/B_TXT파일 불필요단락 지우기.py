import re
import os

def extract_string(target):
    return re.sub('<[^>]*>','',target)

def Delete_BOM(target):
    target.replace(chr(65279),'')


'''폴더내 파일명 리스트 만들기'''

## 폴더내의 파일명을 리스트로 만들기
path = "D:\\Program Files\\Workspace\\00_Default\\"
# path2 = "D:\\Program Files\\Workspace\\00_Create\\"
filenames = os.listdir(path)

## 파일명리스트(filename)에서 txt or srt파일 골라내기.
srt_file = []                       # 골라낸 파일 리스트
for i in filenames:
    if '.srt' in i:              # 'txt' or 'srt'가 포함되어있는 리스트 골라내기
        srt_file.append(i)
## 파일명리스트(filename)에서 txt or srt파일 골라내기.
txt_file = []                       # 골라낸 파일 리스트
for i in filenames:
    if '.txt' in i:              # 'txt' or 'srt'가 포함되어있는 리스트 골라내기
        txt_file.append(i)
## 파일명리스트(filename)에서 txt or srt파일 골라내기.
xml_file = []                       # 골라낸 파일 리스트
for i in filenames:
    if '.xml' in i:              # 'txt' or 'srt'가 포함되어있는 리스트 골라내기
        xml_file.append(i)


''' TXT파일 불필요문구 제거 '''

for file in txt_file:                                       # file : E01_How.txt
    with open(f'{path}{file}','r',encoding = 'utf8') as fr:
        data = fr.readlines()
        for l in data:
            p = extract_string(l.strip()) # < > 안의 데이터 모두 삭제
            if p != '': # 빈칸 삭제
                if ord(p[0:1]) != 65279:
                    with open(f'{path}New_{file}', 'a', encoding='utf8') as fl:
                        fl.write(p.strip())
                        fl.write('\n')

''' xml파일 불필요문구 제거 '''
for file in xml_file:                                       # file : E01_How.txt
    with open(f'{path}{file}','r',encoding = 'utf8') as fr:
        data = fr.readlines()
        for l in data:
            p = extract_string(l.strip()) # < > 안의 데이터 모두 삭제
            if p != '': # 빈칸 삭제
                if ord(p[0:1]) != 65279:
                    with open(f'{path}New_{file}', 'a', encoding='utf8') as fl:
                        fl.write(p.strip())
                        fl.write('\n')
