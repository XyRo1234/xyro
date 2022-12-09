# encoding='UTF8'
# encoding='euc-kr'

#폴더내 파일들 리스트로 정리하기
from os import walk, write     # os안의 walk를 가져와서 사용
# for A in B : B의 index들을 꺼내서 A에 넣은 후, 실행. 리스트 끝까지.

## 폴더내의 파일명을 리스트로 만들기
filename = []
for (dirpath, dirnames, filenames) in walk(r"D:\\Program Files\\Workspace\\00_Default"):   #정리할 파일 위치
    filename.extend(filenames)
    break

## 파일명리스트(filename)에 있는 모든 파일 사용
textfile = []
textfile = filename
#print(textfile)


## 파일명리스트(filename)에서 txt or srt파일 골라내기.
# textfile = []
# for i in filename:
#    if '.txt' in i:              # 'txt' or 'srt'가 포함되어있는 리스트 골라내기
#        textfile.append(i)

# 파일명리스트(filename)에서 txt or srt파일 골라내기.
# textfile = []
# for i in filename:
#    if '.srt' in i:              # 'txt' or 'srt'가 포함되어있는 리스트 골라내기
#        textfile.append(i)





## 파일내 단어수정
for TXTSSML in textfile:
    # print(TXTSSML)
    src1 = "’"                                          # 기존내용
    tar1 = "'"                                          # 바꾸려는 내용
    src2 = "‘"                                          # 기존내용
    tar2 = "'"                                          # 바꾸려는 내용    
    src3 = " "                                          # 기존내용
    tar3 = " "                                          # 바꾸려는 내용

    filepath = ("D:\\Program Files\\Workspace\\00_Default\\" + TXTSSML)
    with open(filepath, "r", encoding='utf-8') as file:           # r : read
        content = file.read()
        content = content.replace(src1, tar1)
        content = content.replace(src2, tar2)
        content = content.replace(src3, tar3)

    filepath2 = ("D:\\Program Files\\Workspace\\00_Create\\" + TXTSSML)
    with open(filepath2, "a", encoding='UTF-8-SIG') as file:           # w : write / a : append
        file.write(content)

