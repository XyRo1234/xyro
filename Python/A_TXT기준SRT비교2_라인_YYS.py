import os, re
from datetime import datetime

srt_path = './0_srt'
txt_path = './0_txt'

def extract_string(target):
    return re.sub('<[^>]*>','',target)

srt_file = os.listdir(srt_path) #txt 확장자 파일 리스트
txt_file = os.listdir(txt_path) #srt 확장자 파일 리스트

txt = {}
for file in txt_file:
    path = f'{txt_path}/{file}'
    with open(path,'r',encoding = 'utf8') as fr:
        data = fr.readlines()
        r = []
        for l in data:            
            p = extract_string(l.strip())
            if p != '':
                r.append(p)
        txt[file] = r
srt = {}
for file in srt_file:
    path = f'{srt_path}/{file}'
    with open(path,'r',encoding = 'utf8') as fr:
        data = fr.readlines()
        r = []
        for l in data:
            line = l.strip()
            try:        
                if line.isdigit():                 
                    continue
                elif datetime.strptime(line[:8],'%H:%M:%S'):            
                    continue       
            except ValueError:
                if line != '':
                    r.append(line)
        srt[file] = r
for x in txt.keys():
    f = x.split('.')
    name = '.'.join(f[:-1])
    srtname = f'{name}.srt'
    
    try:
        for i,srt_line in enumerate(srt[srtname]):            
            if srt_line.strip() == txt[x][i].strip():                
                continue
            else:
                print(f'No Match line : {i}\n{srtname} : {srt_line} \n{x} : {txt[x][i]}')
            
    except KeyError:
        continue
