from msilib.schema import Error
import os
import pandas as pd
import openpyxl
import csv

"""
엑셀통합파일의 각 시트(A열 영어원본,B열 영어수전본,C열 프랑스어)에서, 각각시트별로 txt파일로 생성하기
"""

path = 'D:\\Program Files\\Workspace\\00_Default\\'
path2 = "D:\\Program Files\\Workspace\\00_Create\\"
filenames_draft = os.listdir(path)

filenames = []                    # 골라낸 파일넣을 리스트 생성
for i in filenames_draft:
    if '.xlsx' in i:              # 파일확장자 리스트 골라내기
        filenames.append(i)
filenames.sort()                  # 리스트 abc순 정렬

wb = openpyxl.load_workbook(f'{path}{filenames[0]}')
# sheet = wb.active
get_sheet_names = wb.get_sheet_names()

""" Pandas를 이용해서 각 시트를 txt파일로 만들기"""
# for sheet_name in get_sheet_names:
#     df = pd.read_excel(f'{path}{filenames[0]}', sheet_name = sheet_name)
#     df_column = df[['en-Modity']]
#     try:
#         df_column.to_csv(f'{path2}{sheet_name}.txt', encoding='utf-8', header = False, index = False, quoting=csv.QUOTE_NONE, sep="\t", quotechar="",  escapechar="\\")
#     except:
#         print(df_column)
#         df_column.to_csv(f'{path2}{sheet_name}.txt', encoding='utf-8', header = False, index = False)
#     print(sheet_name)

""" Openpyxl을 이용해서 각 시트를 txt파일로 만들기 """
for sheet_name in get_sheet_names:
    sheet = wb[sheet_name]              # 해당시트명의 시트 열기
    for x in range(2, sheet.max_row + 1):       # 행열 지정. 해더날림.
        value = sheet[f'B{x}'].value
        try:
            with open(f'{path2}{sheet_name}.txt', 'a', encoding='UTF-8-SIG') as file:
                file.write(value)
                file.write('\n')
        except:                                 # 빈칸일 경우 에러가 남. 빈칸은 한줄비움으로 설정.

            with open(f'{path2}{sheet_name}.txt', 'a', encoding='UTF-8-SIG') as file:
                file.write('\n')

    print(sheet_name+'종료')
