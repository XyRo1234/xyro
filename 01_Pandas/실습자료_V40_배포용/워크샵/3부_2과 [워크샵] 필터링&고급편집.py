#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

# - 한셀안의 인쇄동작을 모두 수행
from IPython.core.interactiveshell import InteractiveShell
InteractiveShell.ast_node_interactivity = "all"

# - matplotlib 초기 설정(한글 폰트 설정)
font_name = mpl.font_manager.FontProperties(fname='C:/Windows/Fonts/malgun.ttf').get_name()
mpl.rc('font', family=font_name)


# # << 전국 아파트 거래 현황 데이터 >>
# ## [0]  apart_sale.xlsx'파일 확인하라
# - 전국 월별 아파트 거래 현황 데이터이다. 지역2를 인덱스로 설정한 df_apt이다
# - 2006년 01월 ~ 2022년 11월까지 아파트 거래 자료이다

# In[2]:


# [0]
df_apt = pd.read_excel('apart_sale.xlsx', index_col='지역2')
df_apt.head()
df_apt.info()


# ## [1] df_apt에서 filter메서드를 이용하여 원하는 날짜만 추출하라
# ### 1-1. 매년 1월달 컬럼들을 추출하라(다음 그림 참고(일부임))
# ![image-6.png](attachment:image-6.png)
# ### 1-2. 2022년도 모든 컬럼을 추출하라(다음 그림 참고(일부임))
# ![image-7.png](attachment:image-7.png)

# In[3]:


# [1-1] 코드 작성
df_apt.filter(regex='01$').head()

# [1-2] 코드 작성
df_apt.filter(regex='^22').head()


# ## [2] df_apt에서 서울시 2022년도만 추출하여 df변수에 대입하라
# ### 총계행과 지역1컬럼을 제외한 25행 * 11열로 구성하여 df에 대입한다
# - info()로 확인하라(다음 그림 참고(일부임))
# ![image.png](attachment:image.png)

# In[21]:


# [2] 코드 작성
df = df_apt.query('지역1=="서울"').filter(regex='^22').drop(index='총계')
# df = df_apt.query('지역1=="서울"').filter(regex='^22').iloc[2:,]
# df = df_apt.query('지역1=="서울"').filter(regex='^22').filter(regex='[^총계]',axis=0)

df


# ## [3] 서울시 자치구를 입력받아 df에서 행단위로 추출하라
# ### 3-1. 입력은 공백으로 구분하여 입력받는다(l변수에 대입됨)
# ![image-7.png](attachment:image-7.png)
# ### 3-2. 입력받은 지역의 행들을 추출하라
# - 다음은 예로 ['중구', '송파구', '강동구']을 입력받아 추출된 결과이다
# ![image-9.png](attachment:image-9.png)

# In[22]:


# [3-1] 목록을 참고하여 공백으로 구분하여 여러개 입력 받기
seoul_list = df.index.to_list()
print('[다음은 서울시 지역의 목록이다]\n', seoul_list)
l = input().split()
l


# In[37]:


# [3-2] 코드 작성
# df.query('@l')
df.query('지역2 in @l')


# ## [4] 서울 2022년도 총 거래량으로 등급과 거래율 집계하라
# ### df을 복사한 df2를 이용하여 다음 조건에 따라 처리하라
# ### 1. 서울시 2022년도 총거래량을 집계한 'sum'컬럼을 첫번째로 df2에 추가한다
# ### 2. 'sum'컬럼에서 기준 거래량에 따라 3등급으로 분류하여 'level'컬럼을 두번째로 df2에 추가한다
# - 기준은 2천건 이상이면 'high', 천건 ~ 2천건 미만이면 'mid', 천건 미만이면 'low'로 평가한다
# 
# ### 3. 'sum'컬럼에서 서울시 총거래량('sum'컬럼 합계) 대비 자치구별 거래율로 집계하여 'rate'컬럼을 세번째로 df2에 추가한다
# - 거래율 = 자치구 총거래량 / 서울시 총거래량 
# - 예로 종로구 324거래량을 서울시 총거래량(37859)으로 나누면 0.86% 거래율로 집계됨
# - 거래율 결과값을 소수점이하 2자리까지 백분율로 표기한다
# - 다음 그림 참고(일부)
# ![image-14.png](attachment:image-14.png)

# In[60]:


df2 = df.copy()

# [4] 코드 작성

df2.insert(0,'sum',df2.apply(sum, axis=1))
df2.insert(1, 'level', df2['sum'].map(lambda x: 'high' if x>=2000 else 'mid' if x>=1000 else 'low'))
def func2(x,y):
#     return f'{x/y:.2%}'
    return "{:.2%}".format(x/y)
df2.insert(2, 'rate', df2['sum'].apply(func2, y=df2['sum'].sum()))
df2


# ## [5] 서울 2022년도 거래량 df을 3분기로 재구성하라
# ### 1분기(1 ~ 4월), 2분기(5 ~ 8월), 3분기(9 ~ 11월)로 재 집계하여 새로운 데이터프레임을 구성한다
# - 주어진 func함수를 분석하여 df 데이터프레임에 apply로 적용한다
# - func()함수는 1분기(1 ~ 4월), 2분기(5 ~ 8월), 3분기(9 ~ 11월)로 재 합산한 목록을 리턴한다
# - 집계된 1~3분기 컬럼명은 ['1Q','2Q','3Q']으로 지정한다
# - 다음 그림 참고(일부)
# ![image-6.png](attachment:image-6.png)

# In[61]:


df.head(2)

def func(x):
    return [ x[:'22_04'].sum(), x['22_05':'22_08'].sum(),x['22_09':].sum() ]

# [5] 코드 작성
# ndf = pd.DataFrame(index=df.index, columns=['1Q','2Q','3Q'])
# ndf[['1Q','2Q','3Q']] = df.apply(func, axis=1, result_type='expand')
# ndf.head()
df3 = df.apply(func, axis=1, result_type='expand')
df3.columns = ['1Q','2Q','3Q']
df3.head()


# ## [6] 전국 2022년도 자료에서 불필요한 행들을 제거하라
# ### 전국 2022년도 아파트 거래 자료만 추출한 df2를 이용하여 다음 조건을 처리하라
# ### 6-1. '지역2' 컬럼내 '총계'를 누락처리하라. 
# - '총계'값을 누락처리하여 '총계'행도 제거대상에 포함시키려 한다. 19개행이 존재한다
# - mask나 where를 이용한다
# ![image-2.png](attachment:image-2.png)

# In[65]:


df2 = pd.read_excel('apart_sale.xlsx').filter(regex='지역1|지역2|^22')
print('총계 행 개수 ==> ', df2['지역2'].eq('총계').sum() )
df2.head(4)

# [6-1] 코드 작성
df2['지역2'] = df2['지역2'].mask(df2['지역2']=='총계')
# df2 = df2.replace('총계', np.nan)
df2.head()


# ### 6-2. 행단위로  한개이상 누락된 경우 해당 행을 삭제하라
# - 거래량이 누락된 지역은 없어진 지역으로 '총계'행 포함하여 제거대상이다
# - dropna()를 이용하여 행단위 제거한다
# - 298행중 누락된 행 37행이 제거되어 261개 행이 남는다
# - 다음 그림은 마지막 5개행을 예시로 보여줌(일부)
# ![image.png](attachment:image.png)

# In[70]:


print('누락된 행 개수 ==> ', df2.isna().any(axis=1).sum())
df2.tail() # 마지막 5개행 

# [6-2] 코드 작성
df2.dropna(axis=0).tail()


# In[ ]:




