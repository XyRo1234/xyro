import os



def convert_size(size_bytes):
    import math
    if size_bytes == 0:
        return "0B"
    size_name = ("B", "KB", "MB", "GB", "TB", "PB", "EB", "ZB", "YB")
    i = int(math.floor(math.log(size_bytes, 1024)))
    p = math.pow(1024, i)
    s = round(size_bytes / p, 2)
    return "%s %s" % (s, size_name[i])

path1 = "D:\\1_공통기술5팀\\05_Translate\\Text_TTS_Length_Check\\오디오"
path2 = "D:\\1_공통기술5팀\\05_Translate\\Text_TTS_Length_Check\\일반 텍스트"

audio = os.listdir(path1)
for i,file in enumerate(audio):
    file_size = os.path.getsize(path1+'\\'+file)
    # print('File Size:', file_size, 'bytes')
    print(file+' File Size:', convert_size(file_size), 'bytes')

text = os.listdir(path2)
for i,file in enumerate(text):
    with open(f'{path2}\\{file}','r',encoding = 'utf8') as fr:
        data = fr.readlines()[0]
        print(len(data))









