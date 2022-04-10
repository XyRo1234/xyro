# pip install chardet
import chardet
from chardet import detect
import os

path = "D:\\Program Files\\Workspace\\00_Create\\"
filenames = os.listdir(path)
# print(filenames)

def get_encoding_type(path, filename):
    with open(f'{path}{filename}', "rb") as file:      # read byte
        rawdata = file.read()
        charset = detect(rawdata)['encoding']
    print(f'{filename.ljust(70)} : {charset.rjust(10)}')
    return None

for filename in filenames:
    get_encoding_type(path, filename)