# pip install docx2txt
import docx2txt
import os
from os import walk
from datetime import datetime

path = 'D:\\9_TM\\00_Files\\LGECI RF_3\\'
filenames_draft = os.listdir(path)
filenames = []                    # 골라낸 파일 리스트
for i in filenames_draft:
    if '.docx' in i:              # 'txt' or 'srt'가 포함되어있는 리스트 골라내기
        filenames.append(i)
filenames.sort()


for filename in filenames:
    name = []
    name = filename.split('.')
    data = docx2txt.process(f'{path}{filename}')
    with open(f'{path}{name[0]}.txt', 'w', encoding='utf-8') as fl: # data를 txt파일을 생성해서 쓰기 (data.readlines()가 안되서 하는 작업임)
        fl.write(data)
    with open(f'{path}{name[0]}.txt', 'r', encoding='utf-8') as fl: # txt파일의 내용을 다시 불러와서 readlines 진행
        data = fl.readlines()
    with open(f'{path}{name[0]}.txt', 'w', encoding='utf-8') as fl: # 파일안의 내용 지우기
        pass
    for l in data:       #######  여기서부터는 srt 불필요단락 지우기에서 가져와서 조금만 수정함 ######
        line = l.strip() # 양옆의 빈칸 삭제
        try:
            if line.isdigit(): # 숫자만 있는 것인지 확인
                continue
            elif datetime.strptime(line[:8],'%H:%M:%S'): #문자열의 8자리를 datetime으로 변환을 하여 되는지 안되는지 확인
                continue
        except ValueError:  # 정상적인 문자열이 for 문에서 except를 발생하여 정상 데이터를 저장함
            if line != '':
                if ord(line[0:1]) != 65279:
                    with open(f'{path}{name[0]}.txt', 'a', encoding='utf-8') as fl:
                        fl.write(line.strip())
                        fl.write('\n')