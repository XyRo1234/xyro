import os
import re
import shutil
import datetime


path = "C:\\Users\\USER\\Documents\\Export Files"
path2 = "C:\\Users\\USER\\Documents\\Export Files\\00_모음"
dnow = datetime.datetime.now()


filename_list = []                       # 파일명 리스트
for (dirpath, dirnames, filenames) in os.walk(path):   #정리할 파일 위치
    print(dirpath)
    print(filenames)
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


    '''srt파일명 변경'''
    for i in filenames:
        if '.srt' in i:              # 'xlsx'가 포함되어있는 리스트 골라내기
            srt_name = i                             # (SRT)E05.srt
            m = re.compile("E\d{2}").search(i)       # <re.Match object; span=(12, 15), match='E05'>
            episode = m.group()                      # E05
            srt_rename = dirpath+"\\"+"(SRT)BF_VB_("+lang+")_"+episode+"_"+dnow.strftime("%y%m%d")+".srt"    # 제품군_제품명_ 에피소드No_Title _(언어코드)_날짜.srt
            os.rename(dirpath+"\\"+srt_name, srt_rename)                                                # 제품군_제품명_ 에피소드No_Title _(언어코드)_날짜.srt
            print(srt_rename)
            shutil.copy(srt_rename, path2)   # 파일옴기기

    '''SSML파일명 변경'''
    for i in filenames:
        if '.txt' in i:              # 'xlsx'가 포함되어있는 리스트 골라내기
            ssml_name = i                             # (SRT)E05.srt
            m = re.compile("E\d{2}").search(i)       # <re.Match object; span=(12, 15), match='E05'>
            episode = m.group()                      # E05
            ssml_rename = dirpath+"\\"+"BF_VB_("+lang+")_"+episode+"_"+dnow.strftime("%y%m%d")+".txt"    # 제품군_제품명_ 에피소드No_Title _(언어코드)_날짜.srt
            os.rename(dirpath+"\\"+ssml_name, ssml_rename)                                                # 제품군_제품명_ 에피소드No_Title _(언어코드)_날짜.srt
            print(ssml_rename)
            shutil.copy(ssml_rename, path2)  # 파일옴기기
