#폴더내 파일들 리스트로 정리하기
from os import walk     # os안의 walk를 가져와서 사용
# for A in B : B의 index들을 꺼내서 A에 넣은 후, 실행. 리스트 끝까지.
# UTF8
# UTF16
# cp949


path = "D:\\Program Files\\Workspace\\00_Default\\" #정리할 파일 위치

'''폴더내 파일명 리스트 만들기'''

## 폴더내의 파일명을 리스트로 만들기
filename = []                       # 파일명 리스트                     
for (dirpath, dirnames, filenames) in walk("D:\\Program Files\\Workspace\\00_Default"):   #정리할 파일 위치
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


for TXTSSML in txt_file:
    # print(TXTSSML)
    file= open("D:\\Program Files\\Workspace\\00_Default"+'\\'+ TXTSSML, encoding='UTF8')  # (열는파일명,r:읽기명령) (정리할 파일 위치)
    data=file.read()
    file= open("D:\Program Files\Workspace\extend.txt", "a", encoding='UTF8')      # "a" append    #(파일위치 및 파일생성)
    file.write("<EPISODE> <" + TXTSSML + ">\n")
    file.write(data+"\n")
    file.write("\n")
    file.close()

for TXTSSML in srt_file:
    # print(TXTSSML)
    file= open("D:\\Program Files\\Workspace\\00_Default"+'\\'+ TXTSSML, encoding='UTF8')  # (열는파일명,r:읽기명령) (정리할 파일 위치)
    data=file.read()
    file= open("D:\Program Files\Workspace\extend.srt", "a", encoding='UTF8')      # "a" append    #(파일위치 및 파일생성)
    file.write("<EPISODE> <" + TXTSSML + ">\n")
    file.write(data+"\n")
    file.write("\n")
    file.close()

