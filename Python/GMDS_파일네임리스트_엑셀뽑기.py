import pandas as pd
import os
from openpyxl.styles import Font, Border, Side, PatternFill, Alignment
from openpyxl import load_workbook
import numpy as np
import re

"각 에피소드 파일들의 파일명을, 일일히 복사붙여넣기하기 불편해서, 엑셀로 뽑는 코드"

Create_path = 'D:\\Program Files\\Workspace\\00_Create\\'

draft_filenames = os.listdir(Create_path)

filenames = []                       # 골라낸 파일 리스트
for i in draft_filenames:
    if '.txt' in i:              # 'txt' or 'srt'가 포함되어있는 리스트 골라내기
        filenames.append(i)
filenames.sort()


dic = {'file name': filenames}

df = pd.DataFrame.from_dict(dic, orient='index')
df = df.transpose()     # DataFrame 행열 전환
print(df)
df.to_excel(f'{Create_path}filename.xlsx')
