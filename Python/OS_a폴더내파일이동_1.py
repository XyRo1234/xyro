import os
import re
import shutil


path = "C:\\Users\\USER\\Documents\\Export Files"
path2 = "C:\\Users\\USER\\Documents\\Export Files\\00_모음"

filename_list = []                       # 파일명 리스트
for (dirpath, dirnames, filenames) in os.walk(path):   #정리할 파일 위치
    # print(dirpath)
    # print(dirnames)
    # print(filenames)

    p = re.compile("[a-zA-Z]{2}-[a-zA-Z0-9_]{2}")    # re.compile('..-[a-zA-Z]{2}')
    m = p.search(dirpath)         # ex)  <re.Match object; span=(0, 5), match='ar-AE'>
    if m:
        # print(dirpath)
        # print(filenames)
        for i in filenames:
            print(i)
            # shutil.move(dirpath+"\\"+i, path2) # 파일옴기기
            shutil.copy(dirpath+"\\"+i, path2) # 파일복사

