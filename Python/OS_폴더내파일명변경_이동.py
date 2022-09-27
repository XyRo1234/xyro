import os
import re
import shutil


path = "C:\\Users\\USER\\Documents\\Export Files"

filename_list = []                       # 파일명 리스트
for (dirpath, dirnames, filenames) in os.walk(path):   #정리할 파일 위치
    # print(dirpath)
    # print(filenames)
    p = re.compile("[a-zA-Z]{2}-[a-zA-Z0-9_]{2}")    # re.compile('..-[a-zA-Z]{2}')
    m = p.search(dirpath)         # ex)  <re.Match object; span=(0, 5), match='ar-AE'>
    try:    
        lang = m.group()                  # ex)  ar-AE
    except:
        continue

    if p.search(filenames[0]):
        pass

    if lang == 'es-41':
        lang = 'es-419'
    elif lang == 'uz-La':
        lang = 'uz-Latn-UZ'
    elif lang == 'az-La':
        lang = 'az-Latn-AZ'
    elif lang == 'bs-La':
        lang = 'bs-Latn-BA'
    elif lang == 'sr-La':
        lang = 'sr-Latn-RS'
    else:
        lang = lang

    if m:
        b = dirpath + '\\' + filenames[0]
        os.rename(dirpath+"\\"+filenames[0], dirpath+"\\"+lang+"_"+filenames[0])

    shutil.move(dirpath+"\\"+lang+"_"+filenames[0], path) # 파일옴기기
