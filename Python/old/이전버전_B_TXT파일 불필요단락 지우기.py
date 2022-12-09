from os import walk
import re
path = "D:\\Program Files\\Workspace\\00_Default\\"

def extract_string(target):
    return re.sub('<[^>]*>','',target)


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

''' TXT파일 불필요문구 제거 '''

txt = {}
for file in txt_file:                                       # file : E01_How.txt
    # path = f'{txt_path}/{file}' #txt파일의 경로
    with open(f'{path}{file}','r',encoding = 'utf8') as fr:
        data = fr.readlines()
        r = set() #집합 함수로 데이터를 저장하기 위해 변수 선언
        for l in data:
            p = extract_string(l.strip()) # < > 안의 데이터 모두 삭제
            if p != '': # 빈칸 삭제
                r.add(p.strip())
                with open(f'{path}New_{file}', 'a', encoding='utf8') as fl:
                    fl.write(p.strip())
                    fl.write('\n')

        txt[file] = r # 파일명 : value로 저장
