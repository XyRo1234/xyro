import os, re
from datetime import datetime

srt_path = './0_srt'
txt_path = './0_txt'

def extract_string(target):
    return re.sub('<[^>]*>','',target)


srt_file = os.listdir(srt_path) #txt 확장자 파일 리스트
txt_file = os.listdir(txt_path) #srt 확장자 파일 리스트

txt = {}
'''txt file string preprocessing'''
for file in txt_file:
    path = f'{txt_path}/{file}' #txt파일의 경로
    with open(path,'r',encoding = 'utf8') as fr:
        data = fr.readlines()
        r = set() #집합 함수로 데이터를 저장하기 위해 변수 선언
        for l in data:
            p = extract_string(l.strip()) # < > 안의 데이터 모두 삭제
            if p != '': # 빈칸 삭제
                r.add(p.strip())
        txt[file] = r # 파일명 : value로 저장
        
'''srt file string preprocessing'''
srt = {}
for file in srt_file:
    path = f'{srt_path}/{file}' #srt파일의 경로
    with open(path,'r',encoding = 'utf8') as fr: 
        data = fr.readlines()
        r = set() #집합 함수로 데이터를 저장하기 위해 변수 선언
        for l in data:
            line = l.strip() # 양옆의 빈칸 삭제
            try:        
                if line.isdigit(): # 숫자만 있는 것인지 확인    
                    continue
                elif datetime.strptime(line[:8],'%H:%M:%S'): #문자열의 8자리를 datetime으로 변환을 하여 되는지 안되는지 확인
                    continue       
            except ValueError:  # 정상적인 문자열이 for 문에서 except를 발생하여 정상 데이터를 저장함
                if line != '':
                    r.add(line.strip())
        srt[file] = r
        
'''srt,txt file text string check '''
for x in txt.keys(): # txt파일명으로 저장한 dictinoary의 키값을 iterable for문
    f = x.split('.')
    name = '.'.join(f[:-1])
    srtname = f'{name}.srt'    
    
    try:
        if srt[srtname]: # srt파일명 중 txt와 동일한 파일명이 존재하는지 확인
            for txt_line in txt[x]:  # txt의 string 값이 srt파일에 존재하는지 확인 없을 시 No Match line으로 출력          
                if txt_line in srt[srtname]:                                 
                    continue
                else:
                    print(f'No Match line, {x} : {txt_line}')            
    except KeyError: # 동일한 파일명이 없을 시 Keyerror가 발생함
        continue
