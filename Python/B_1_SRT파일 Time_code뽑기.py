from os import walk
from datetime import datetime

path = "D:\\Program Files\\Workspace\\00_Default\\"

'''폴더내 파일명 리스트 만들기'''

## 폴더내의 파일명을 리스트로 만들기
filename = []                       # 파일명 리스트                     
for (dirpath, dirnames, filenames) in walk(r"D:\\Program Files\\Workspace\\00_Default"):   #정리할 파일 위치
    filename.extend(filenames)
    break
# print(filename)

## 파일명리스트(filename)에서 txt or srt파일 골라내기.
srt_file = []                       # 골라낸 파일 리스트
for i in filename:
    if '.srt' in i:              # 'txt' or 'srt'가 포함되어있는 리스트 골라내기
        srt_file.append(i)
## 파일명리스트(filename)에서 txt or srt파일 골라내기.
txt_file = []                       # 골라낸 파일 리스트
for i in filename:
    if '.txt' in i:              # 'txt' or 'srt'가 포함되어있는 리스트 골라내기
        txt_file.append(i)


''' SRT파일 불필요문구 제거 '''
for file in srt_file:                                       # file : E01_How.srt
    # txtfile = file.split(".")[0]
    with open(f'{path}{file}','r',encoding = 'utf8') as fr:
        data = fr.readlines()
        for l in data:
            line = l.strip() # 양옆의 빈칸 삭제
            try:
                if line.isdigit(): # 숫자만 있는 것인지 확인
                    continue
                elif datetime.strptime(line[:8],'%H:%M:%S'): #문자열의 8자리를 datetime으로 변환을 하여 되는지 안되는지 확인                    
                    with open(f'{path}Time_Code_{file}', 'a', encoding='utf8') as fl:
                    # with open(f'{path}{txtfile}.txt', 'a', encoding='utf8') as fl:
                        fl.write(line.strip())
                        fl.write('\n')
            except ValueError:  # 정상적인 문자열이 for 문에서 except를 발생하여 정상 데이터를 저장함
                if line != '':
                    if ord(line[0:1]) != 65279:
                        with open(f'{path}New_{file}', 'a', encoding='utf8') as fl:
                        # with open(f'{path}{txtfile}.txt', 'a', encoding='utf8') as fl:
                            fl.write(line.strip())
                            fl.write('\n')
