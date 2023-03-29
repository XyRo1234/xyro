#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pandas as pd
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

# - 한셀안의 인쇄동작을 모두 수행
from IPython.core.interactiveshell import InteractiveShell
InteractiveShell.ast_node_interactivity = "all"


# ### [1] 기상자료 데이터셋을 읽어와 df변수에 저장하는 다음 코드를 실행하여 이해하라
# 1. 기상자료 데이터셋 
# - 'suwon_weather.csv' 파일은 2000-01-01 ~ 2021-12-31기간까지 수원지역 기상자료이다
# - 만약 CSV 파일이 UTF-8이 아닌 ANSI 형식일 경우 encoding 옵션을 사용하여 ANSI 형식으로 지정하라
# 2. parse_dates 옵션 이해
# - '날짜'컬럼을 DatetimeIndex로 지정하는 방법으로 read_csv()에서 parse_dates=True 옵션을 이용한다

# In[4]:


col = ['날짜', '지점', '평균','최저','최고'] # 컬럼명
df = pd.read_csv('suwon_weather.csv', encoding='ANSI', header=6, names=col, \
                 index_col='날짜', parse_dates=True)
df.head()
df.index


# ### [2] df['최고'] 컬럼에서 특정 날짜를 인덱싱하기
# 1. df['최고'] 컬럼 sr에서 2021년 6월 1일 날짜의 최고 기온을 확인하라
# 2. df['최고'] 컬럼 sr에서 2021년도 6월달 한달간 최고 기온을 확인하라
# - 아래 그림과 같이 인쇄하라(6월달 데이터는 일부만 인쇄함)
# ![image-5.png](attachment:image-5.png)

# In[12]:


# df['최고'] 컬럼 sr에서 2021년 6월 1일 날짜의 최고 기온을 확인하라
# df['최고'] 컬럼 sr에서 2021년도 6월달 한달간 최고 기온을 확인하라

sr = df['최고']
sr

# [2-1] 코드 작성
sr['2021-06-01']

# [2-2] 코드 작성
sr['2021-06']


# ### [3] 특정 날짜만 선별하여 구성한 Series생성하기
# - df['평균'] 컬럼에서 주어진 idx에 있는 날짜로만(21년도 월초일자) 구성한 새 Series를 생성하여 인쇄하라(다음 그림 참고)
# ![image-2.png](attachment:image-2.png)

# In[26]:


idx = pd.date_range('2021-1-1', '2021-12-31', freq='MS')
idx

# [3] 코드 작성
sr2 = pd.Series(df['평균'],index=idx)
sr2


# ### [4] 특정 날짜만 선별하여 DataFrame 생성하기 
# 1. 2000-1-1 ~ 2021-12-31 기간중 freqnucy를 년초일자(1월1일)로 지정한 DatetimeIndex를 생성하여 변수 idx에 대입하라
# - (참고) 년초일자(1월1일)의 frequency string은 'AS'를 사용한다
# 2. idx 변수를 이용하여 df에서 해당 idx에 포함된 일자의 데이터를 추출한 데이터프레임을 new_df에 대입하라
# - 아래 그림과 같이 나오도록 idx와 new_df의 내용을 확인하라(new_df결과는 일부만 인쇄함)
# ![image-5.png](attachment:image-5.png)

# In[33]:


# 2000-1-1 ~ 2021-12-31 기간중 freqnucy를 년초일자(1월1일)로 지정한 DatetimeIndex를 생성하여 변수 idx에 대입하라
# (참고) 년초일자(1월1일)의 frequency string은 'AS'를 사용한다
# idx 변수를 이용하여 df에서 해당 idx에 포함된 일자의 데이터를 추출한 데이터프레임을 new_df에 대입하라
# 아래 그림과 같이 나오도록 idx와 new_df의 내용을 확인하라(new_df결과는 일부만 인쇄함)

# [4-1] 코드 작성
idx = pd.date_range('2000-01-01','2021-12-31',freq='AS')
idx
# [4-2] 코드 작성
new_df = pd.DataFrame(df, index=idx)
new_df


# ### [5] 여러 DataFrame을 엑셀 파일의 각 시트로 저장하는 다음 코드를 이해하라
# #### DataFrame.to_excel( excel_writer , sheet_name = 'Sheet1', ... )  
# 1. 여러 시트에 쓰려면 쓸 파일을 pd.ExcelWriter(file)로 ExcelWriter개체를 만든다
# 2. df.to_excel(ExcelWriter 개체, sheet_name=시트명)로 df을 시트단위로 파일에 저장한다
# 3. 다음 코드를 실행하여 newfile1을 엑셀에서 열어 확인하라

# In[34]:


newfile1 = 'newfile1.xlsx'
df1 = df.nlargest(5, '최고')
df2 = df.nsmallest(5, '최저')

with pd.ExcelWriter(newfile1) as writer :
    df1.to_excel(writer, sheet_name="최고기온")
    df2.to_excel(writer, sheet_name="최저기온")


# ### [6] 2개의 데이터프레임을 엑셀에 시트별로 저장하고 읽기
# 1. 다음 조건으로 2개의 데이터프레임을 생성하라
# - 2020년도 1월 ~ 12월까지 월초일자 간격으로 12개의 날짜로 구성한 df1
# - 2020년도 1월 ~ 12월까지 월말일자 간격으로 12개의 날짜로 구성한 df2
# 2. df1과 df2인 2개의 DataFrame을 newfile2 파일에 '월초기온', '월말기온' sheet명으로 지정하여 저장하라
# - 아래 그림은 저장한 newfile2를 엑셀에서 열어서 확인한 결과이다
# ![image.png](attachment:image.png)   
#     
# 3. newfile2 파일에서 '월말기온'sheet를 읽어와 df3에 대입하라
# - 아래 그림의 결과처럼 동일한 결과로 df3을 읽어와 인쇄한다.(인쇄결과는 일부임)
# ![image-3.png](attachment:image-3.png)

# In[39]:


# 다음 조건으로 2개의 데이터프레임을 생성하라
# 2020년도 1월 ~ 12월까지 월초일자 간격으로 12개의 날짜로 구성한 df1
# 2020년도 1월 ~ 12월까지 월말일자 간격으로 12개의 날짜로 구성한 df2

# [6-1] 코드 작성
idx = pd.date_range('2020-01-01','2020-12-31',freq='MS')
df1 = pd.DataFrame(df,index=idx)
df1
idx = pd.date_range('2020-01-31','2020-12-31',freq='M')
df2 = pd.DataFrame(df,index=idx)
df2


# In[41]:


# df1과 df2인 2개의 DataFrame을 newfile2 파일에 '월초기온', '월말기온' sheet명으로 지정하여 저장하라
# 아래 그림은 저장한 newfile2를 엑셀에서 열어서 확인한 결과이다

newfile2 = 'newfile2.xlsx'

# [6-2] 코드 작성
with pd.ExcelWriter(newfile2) as writer:
    df1.to_excel(writer, sheet_name='월초기온')
    df2.to_excel(writer, sheet_name='월말기온')


# In[46]:


# newfile2 파일에서 '월말기온'sheet를 읽어와 df3에 대입하라
# 아래 그림의 결과처럼 동일한 결과로 df3을 읽어와 인쇄한다.(인쇄결과는 일부임)

newfile2 = 'newfile2.xlsx'
col = ['날짜', '지점', '평균','최저','최고'] # 컬럼명

# [6-3] 코드 작성
df3 = pd.read_excel(newfile2, sheet_name='월말기온', names=col)
df3


