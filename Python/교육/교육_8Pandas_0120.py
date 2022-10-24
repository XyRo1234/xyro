# https://www.youtube.com/watch?v=ffjpgvAHegk&list=PLVNY1HnUlO26Igldy2Q6Nb2LZbpQWTyle&index=5
from pickle import GLOBAL
import pandas as pd
from collections import OrderedDict
import numpy as np

"""1장 파일에서 data 불러오기(txt파일)"""
# file = pd.read_csv('.\sample.txt')
# file = pd.read_csv('.\sample.txt', delimiter='\t')      # delimiter='\t' : header 구분이 탭으로 되어있는 경우 사용.
# file = pd.read_csv('.\sample.txt', header=None)         # header=None   : header가 없는 경우 해당명령어로 head가 없다고 알려줌
# file.columns = ['name', 'age', 'job']                   # 해더정보를 별도로 입력해서 추가삽입해줌
# file = pd.read_csv('.\sample.txt', header=None, names=['name', 'age', 'job']) # 위의 두줄을 한줄로 사용가능함. [해더없음, 해더정보 별도삽입]
# print(file)

"""3-1장 DataFrame 생성하기. dict """
# friend_dict_list = [{'name': 'Jone', 'age': 20, 'job': 'student'},                            # DataFrame 생성용 Dict 생성1
#                     {'name': 'Jenny', 'age': 30, 'job': 'developer'},
#                     {'name': 'Nate', 'age': 30, 'job': 'teacher'}]
# df = pd.DataFrame(friend_dict_list)                                                           # DataFrame 생성. 단, 이상태에서는 data의 순서는 보장되지않는다고함(column not fixed). 그래서 아랫줄을 실행한다고함.
# df = df[['name', 'age', 'job']]                                                               # data순서를 ['name', 'age', 'job'] 순서로 정렬
# df.head()

# friend_dict_list = [{'age': 20, 'job': 'student'},                                            # DataFrame 생성용 Dict 생성2
#                     {'age': 30, 'job': 'developer'},
#                     {'age': 30, 'job': 'teacher'}]
# df = pd.DataFrame(friend_dict_list, index=['John','Jenny','Nate'], columns=['age','job'])     # index(행) 0,1,2에 값('John','Jenny','Nate')넣기

"""3-2장 DataFrame 생성하기. OrderedDict """
from collections import OrderedDict                                                           # OrderedDict Import하기
friend_ordered_dict = OrderedDict([                                                           # OrderedDict 사용해서 data를 저장. column fixed(data순서) 시킴
            ('name', ['John', 'Jenny', 'Nate']),
            ('age', [20, 30, 30]),
            ('job', ['student', 'developer', 'teacher'])
                                ])
df = pd.DataFrame.from_dict(friend_ordered_dict)                                              # DataFrame 생성.(.from_dict) 사용
# print(df.head())

"""3-3장 DataFrame 생성하기. list """
friend_list = [ ['John', 20, 'student'],['Jenny', 30, 'developer'],['Nate', 30, 'teacher'] ]    # dict 생성
column_name = ['name', 'age', 'job']                                                            # header용 리스트 생성
# df = pd.DataFrame.from_records(friend_list, columns=column_name)                                # from_records로 list, columns(header) 한번에 삽입 생성.
# print(df.head())
en_line_list= []
bb_line_list = []
cc_line_list = []
"""3-3-2장 DataFrame 생성하기. list """
dic = {
    'en-Origin': en_line_list,
    'en-Modify': bb_line_list,
    'fr-CA': cc_line_list
}

df = pd.DataFrame.from_dict(dic, orient='index')
df = df.transpose()     # DataFrame 행열 전환



"""3-4장 DataFrame 생성하기. 버전업 되면서 없어진 함수임. 사용하지말것"""
# friend_list = [                                                                                 
#                 ['name',['John', 'Jenny', 'Nate']],
#                 ['age',[20,30,30]],
#                 ['job',['student', 'developer', 'teacher']]
#               ]
# df = pd.DataFrame.from_items(friend_list)
# print(df.head())

"""4-1장 파일생성"""
# from collections import OrderedDict                                       # OrderedDict Import하기
# friend_ordered_dict = OrderedDict([                                       # OrderedDict 사용해서 data를 저장. column fixed(data순서) 시킴
#             ('name', ['John', 'Jenny', 'Nate']),
#             ('age', [20, 30, 30]),
#             ('job', ['student', 'developer', 'teacher'])
#                                 ])
# df = pd.DataFrame.from_dict(friend_ordered_dict)                          # DataFrame 생성.(.from_dict) 사용
# df.to_csv('friend_list_from_df.csv')                                      # DataFrame 파일생성 (header = True, index = True)이 입력된거랑 같음
# df.to_csv('friend_list_from_df.csv', header = True, index = True)         # DataFrame 파일생성 (header = True, index = True)별도 입력해도 됨
# df.to_csv('friend_list_from_df.csv', header = False, index = False)       # DataFrame 파일생성
# df.to_csv('friend_list_from_df.csv', header = ['name', 'age', 'job'])     # DataFrame 파일생성

"""4-2장 파일생성, None Data 삽입시"""
# from collections import OrderedDict                                       # OrderedDict Import하기
# friend_ordered_dict = OrderedDict([                                       # OrderedDict 사용해서 data를 저장. column fixed(data순서) 시킴
#             ('name', ['John', None, 'Nate']),
#             ('age', [20, None, 30]),
#             ('job', ['student', 'developer', 'teacher'])
#                                 ])
# df = pd.DataFrame.from_dict(friend_ordered_dict)
# df.to_csv('friend_list_from_df.csv', na_rep = '-')                        # DataFrame 파일생성 (None data에는 - 를 삽입해라)

"""5장 DF 행,열(row,column) 선택 및 필터하기 """
# df[1:3]                                                             # select rows from index 1 to index 2

# df.loc[[0,2]]                                                       # select row index 0 and index 2

# df_filtered = df[df.age > 25]                                       # [age>25]인 column data만 가져오기
# print(df_filtered)
# df_filtered = df.query('age>25')                                    # [age>25]인 column data만 가져오기
# print(df_filtered)
# df_filtered = df[(df.age >25) & (df.name == 'Nate')]                # [age>25],[name:Nate]인 column data만 가져오기
# print(df_filtered)

df.columns.values.tolist()  # column(열,해더) 이름 추출
df.rename(columns={'癤풬o':'No'}, inplace=True) # 열이름 변경하기

df = df.loc[:,['fields.Episode','fields.No.','fields.SRT_Time_Code', 'fields.SRT/SSML']]  # 해당 header(columns)만 뽑아서 datafarame 만들기
df = df.loc[(df['fields.Episode'] == 'E01')]                                        # fields.Episode = E01인 행만 뽑기.
df = df.loc[(df['fields.Episode'] == 'E01'), ['fields.Episode','fields.No.','fields.SRT_Time_Code', 'fields.SRT/SSML']] # 위의 2개 합친거.

df.loc[(df['No']==i+1)]['SRT_Time_Code'].values[0]  # No가 i인행의 SRT_Time_Code값 가져옴

print(df.loc[i]['SRT_Time_Code'])                 # name의 0번째 값을 가져옴
print(df.iloc[0]['name'])                         # name의 index가 0인곳의 값을 가져옴
print(df.iat[0,0])
print(df.at[1,'name'])
print(df.at[df.index[-1],'name'])                 # name의 -1번째 값을 가져옴
print(df['name'].values[0])                    

# df.iloc[:, 0:2]                                 # select all rows, from column 0 to column 1
# df.iloc[:,[0,2]]                                # select all rows, column 0 and column 2
# df_filtered = df[['name', 'age']]               # 특정 열만 선택1
# df.filter(items=['age', 'job'])                 # 특정 열만 선택2
# df.filter(like='a',axis=1)                      # 특정 열만 선택3 (header에 a가 들어있는 열) (axis=1 '열'이라는 뜻) axis=0 -> column, axis=1 -> row 이다. 
# df.filter(regex='b$',axis=1)                    # 특정 열만 선택4 (header가 b로 끝나는 열(b$:정규식)) (axis=1 '열'이라는 뜻)

"""6장 DF 행,열(row,column) 삭제하기 """
# df.drop(['John', 'Nate'])                       # header의 ['John', 'Nate']인 열 삭제
# df = df.drop(['John', 'Nate'])                  # df에 삭제한 data 넣기1
# df.drop(['John', 'Nate'], inplace = True)       # df에 삭제한 data 넣기2 (inplace를 이용하여 한줄로 줄일수있음)
# df = df.drop(df.index[[0,2]])                   # Index(행) 0,2번째행 삭제하기
# df = df.drop('age', axis=1)                     # 열에서 age를 찾아서 그열을 삭제 (axis=1 '열'이라는 뜻)



"""7장 DF 행,열 생성 및 수정하기 """
"""7-1-1장 DF 열 생성 및 수정하기 (numby사용) """
# df['salary'] = 0                                                                # 열에 salary 추가. 밑에 값들은 0으로 들어감.
# import numpy as np
# df['salary'] = np.where(df['job'] != 'student' , 'yes', 'no')                   # job열을 불러와서 student가 아니면 yes, 그외 no를 삽입.

"""7-1-2장 DF 열 생성 및 수정하기 (수식을 사용하여 값 넣기) """
# friend_dict_list = [{'name': 'John', 'midterm': 95, 'final': 85},               # 중간고사(midterm), 기말고사(final) 점수가 있는 df생성
#          {'name': 'Jenny', 'midterm': 85, 'final': 80},
#          {'name': 'Nate', 'midterm': 10, 'final': 30}]
# df = pd.DataFrame(friend_dict_list, columns = ['name', 'midterm', 'final'])
# df['total'] = df['midterm'] + df['final']                                       # total 열생성. 값으로 (중간고사+기말고사) 값을 넣음.
# df['average'] = df['total'] / 2                                                 # average 열생성. 값으로 (total/2) 값을 넣음.

"""7-1-3장 DF 열 생성 및 수정하기 (리스트, for문이용, 값생성 및 삽입) """
# grades = []                                                                     # grade 열 생성을 위해, gades 리스트를 제작.
# for row in df['average']:
#     if row >= 90:
#         grades.append('A')
#     elif row >= 80:
#         grades.append('B')
#     elif row >= 70:
#         grades.append('C')
#     else:
#         grades.append('F')
# df['grade'] = grades                                                            # grade 열생성. 값으로 grades 리스트 넣음.

"""7-1-4장 DF 열 생성 및 수정하기 (함수생성. apply적용한 값으로 열생성1) """
# def pass_or_fail(row):
#     print(row)
#     if row != "F":
#         return 'Pass'
#     else:
#         return 'Fail'

# df.grade = df.grade.apply(pass_or_fail)                                         # grade값을 불러와서 적용해라(apply) pass_or_fail함수를.

"""7-2장 DF 열 생성 및 수정하기 (함수생성. apply적용한 값으로 열생성2) """
date_list = [{'yyyy-mm-dd': '2000-06-27'},                  # DataFrame 생성
         {'yyyy-mm-dd': '2002-09-24'},
         {'yyyy-mm-dd': '2005-12-20'}]
df = pd.DataFrame(date_list, columns = ['yyyy-mm-dd'])

def extract_year(row):                                      # extract_year 함수생성
    return row.split('-')[0]                                # -로 나누어서 리스트 생성하고, 0번째 값을 리턴.

df['year'] = df['yyyy-mm-dd'].apply(extract_year)           # apply이용해서 함수적용한 값으로, year열 생성.


"""7-3장 DF 행 생성 및 수정하기 () """
Topic_No_list = ['100','101','102']
Topic_Title_list = ['Title1','Title2','Title3']
Region_list = ['GLOBAL','FRANCE','KOREA']
First_Data = [{'No':Topic_No_list[0], 'Topic Title':Topic_Title_list[0],'Region':Region_list[0]}]   # DF작성
df = pd.DataFrame(First_Data)                                                                       # DF생성
i=1
while i < 100:
    try:
        df.loc[i]=[Topic_No_list[i], Topic_Title_list[i],Region_list[i]]                            # DF에 행추가
        i+=1
    except:
        break


""" na_values 예시 """
df = pd.read_excel("xls_file.xlsx", na_values=["?", "??", "N/A", ""], keep_default_na=False, skipfooter=skip_footer, engine="openpyxl")
# df = df.replace(numpy.nan, '', regex=True)        # NaN값을 빈칸''으로 변환해줌


""" ExcelWriter로 쓰기1 (engine = "openpyxl") """
writer = pd.ExcelWriter(output_folder + r"\GSCS_Data - Case III_#추가.xlsx", engine="openpyxl", options={'strings_to_urls': False})
    df_gscs_info.to_excel(writer, index=False, sheet_name="GSCS_Info", freeze_panes=(1,0))
    workbook = writer.book
    ws = writer.sheets["GSCS_Info"]
    ws.column_dimensions["D"].width = 21
    ws.column_dimensions["F"].width = 9
    ws.column_dimensions["H"].width = 15
    ws.column_dimensions["J"].width = 50
    ws.auto_filter.ref = ws.dimensions
    writer.save()


" "
""" ExcelWriter로 쓰기2 (engine = 'xlsxwriter') """
writer = pd.ExcelWriter(
        output_folder + r"\Model_Data.xlsx",
        engine="xlsxwriter",
        options={'strings_to_urls': False}
    )
    df_md_info.to_excel(writer, index=False, sheet_name="MD_Info")
    (max_row, max_col) = df_md_info.shape
    workbook = writer.book
    ws = writer.sheets["MD_Info"]
    ws.freeze_panes("A2")
    ws.autofilter(0, 0, max_row, max_col)
    writer.save()
