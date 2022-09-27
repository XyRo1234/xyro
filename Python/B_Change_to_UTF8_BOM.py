from chardet import detect
import os

path = "D:\\Program Files\\Workspace\\00_Default\\"
path2 = "D:\\Program Files\\Workspace\\00_Create\\"
filenames = os.listdir(path)
# print(filenames)

def get_encoding_type(path, filename):                  # 인코딩타입 체크함수
    with open(f'{path}{filename}', "rb") as file:      # read byte
        rawdata = file.read()
        charset = detect(rawdata)['encoding']
    #print(f'{filename.ljust(70)} : {charset.rjust(10)}')
    return charset

txt_file = []                       # 골라낸 파일 리스트
for i in filenames:
    if '.txt' in i:              # 'txt' or 'srt'가 포함되어있는 리스트 골라내기
        txt_file.append(i)

for filename in txt_file:
   a = get_encoding_type(path, filename)
   print(a)

for filename in txt_file:
    read_codec = get_encoding_type(path, filename)
    if read_codec == "ISO-8859-1":                  # 외국어중 ISO-8859-1 인코딩으로 뜨는 경우, utf-8로 변경
        with open(f'{path}{filename}', 'r', encoding='ISO-8859-1') as source, open(f'{path2}{filename}', 'w', encoding="utf-8") as target:
            target.write(source.read())
            print("ISO-8859-1 파일있음 확인요망")
    else:                                           # 모든파일 UTF-8 BOM 인코딩으로 변경
        with open(f'{path}{filename}', 'r', encoding=read_codec) as source, open(f'{path2}{filename}', 'w', encoding="UTF-8-SIG") as target:
            target.write(source.read())
            print(f'{filename.ljust(70)} complete')

