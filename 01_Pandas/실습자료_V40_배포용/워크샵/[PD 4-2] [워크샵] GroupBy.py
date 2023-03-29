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


# # << 국내 주식 데이터 >>
# ## [0] 'stock.csv'와 'my_stock.csv' 파일 확인하기
# - 참고 사이트 : http://data.krx.co.kr/contents/MDC/MDI/mdiLoader/index.cmd?menuId=MDC0201 
# 1. df_stock는 코스닥 주식 데이터 'stock.csv' 파일(12행*8열)을 읽어 온 데이터프레임이다
# - 종목코드는 식별코드로 6자리로 이루어져 있고 문자를 포함하고 있어 문자열타입이다   
# - 종목크드는 끝자리가 보통주 일경우 ‘0’, 우선주인 경우는 ‘5’, 'K', 'M'등으로 구성되어 있다
# 2. df_my는 관심있는 종목코드와 종목명으로 구성된 'my_stock.csv'파일(6행*2열)을 읽어온 데이터프레임이다
# - df_stock내에 존재하는 종목코드중 일부의 종목으로 구성되어 있다

# In[2]:


df_stock = pd.read_csv('stock.csv', index_col='종목코드')
df_my = pd.read_csv('my_stock.csv', index_col='종목코드')
df_stock
df_my


# ## [1] df_stock과 df_my를 결합하여 df 변수에 대입하라
# - df_my의 종목코드와 일치하는 행만 df_stock에서 가져와 병합하라
# - 다음 그림을 참고하여 같은 결과가 나오도록 구현하라
# ![image.png](attachment:image.png)

# In[16]:


# [1] 코드 작성
# df = df_stock.loc[df_my.index]
# df = df_my.join(df_stock.loc[:,'업종명':])
df = df_my.merge(df_stock,on=['종목코드','종목명'], how='left')
df


# ## [2] df에서 '업종명'별 평균 집계하라
# ### 1. 업종명별 평균집계를 groupby()로 집계하여 x에 대입하고 확인하라
# - 업종명별 그룹화하고 전 수치 컬럼에 적용한다  
# 
# ### 2. 업종명별 평균 집계를 pivot_table()로 집계하여 y에 대입하고 확인하라
# - 업종명별 그룹화하고 전 수치 컬럼에 적용한다
# 
# ### 3. x와 y의 차이를 확인하라
# - x, y의 dtypes로 확인하고 groupby와 pivot_table의 동작 차이를 검토하여 보자
# ![image.png](attachment:image.png)

# In[30]:


# [2] 코드 작성
x = df.groupby('업종명').mean()
x
x.dtypes
y = df.pivot_table(index='업종명', aggfunc='mean')
y
y.dtypes


# ## [3] df에서 주어진 종목(code)으로만 선별하여 그룹 집계하라
# ### 주어진 종목코드(code)로 선별하여 2개의 그룹별('G1', 'G2') max 집계를 한다. 적용대상으로 종가' '등락률', '시가' 컬럼에만 적용한다
# - 실행 결과는 다음 그림을 참고한다
# ![image.png](attachment:image.png)

# In[28]:


code = {'282330':'G1', '128820':'G1', '145995':'G2','336370':'G2'}

# [3] 코드 작성
df.groupby(code)['종가','등락률','시가'].max()


# ## [4] df에서 등락에 따른 종목의 개수로 집계하라
# ### '등락률' 컬럼에서 등락률이 +인 경우와 -인 경우로 그룹화하여 그룹별 개수로 집계하라. 등락률이 +이면 'up', -이면 'down' 명으로 지정한다
# - (참고) groupby 객체에 size() 메서드를 적용하면 그룹별 행의 수로 집계한다
# ![image.png](attachment:image.png)

# In[49]:


# [4] 코드 작성
df.groupby( np.where(df['등락률']>=0,'up' ,'down') ).size()

# sr = df['등락률'].apply(lambda x : 'up' if x>0 else 'down')
# sr
# df.groupby(sr).size()


# ## [5] df에서 보통주와 우선주별 종목의 개수로 집계하라
# - '종목코드'에서 보통주와 우선주로 그룹화하여 그룹별 개수로 집계한다.
# - (참고) 종목코드는 끝자리가 보통주 일경우 ‘0’, 우선주인 경우는 ‘5’, 'K', 'M'등으로 구성되어 있다
# ![image.png](attachment:image.png)

# In[56]:


# [5] 코드 작성
def func(x):
    return '일반주' if x[-1]=='0' else '우선주'
a = df.groupby(func).size()
a.index.name = None
a

arr = np.where(df.index.str.endswith('0'), '일반주','우선주')
df.groupby(arr).size()


# In[ ]:




