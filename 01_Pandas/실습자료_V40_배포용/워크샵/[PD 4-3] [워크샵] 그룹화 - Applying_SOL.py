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
# ### 주식 데이터 'stock.csv' 파일(12행*8열)을 읽어 온 데이터프레임 df이다
# - 종목코드는 식별코드로 6자리로 이루어져 있고 문자를 포함하고 있어 문자열타입이다   
# - 종목크드는 끝자리가 보통주 일경우 ‘0’, 우선주인 경우는 ‘5’, 'K', 'M'등으로 구성되어 있다
# - 참고 사이트 : http://data.krx.co.kr/contents/MDC/MDI/mdiLoader/index.cmd?menuId=MDC0201   

# In[2]:


df = pd.read_csv('stock.csv', index_col='종목코드')
df


# ## [1] df에서 업종별 최고가와 최저가의 편차로 집계하라
# ### 업종별 '종가', '시가', '거래대금' 각 컬럼에 대하여 최고와 최저가의 편차로 집계하라
# - 예로 유통업 '종가'의 경우 유통업 종가의 최고가 - 최저가로 편차를 구한다
# - 다음 결과를 참고하라
# ![image.png](attachment:image.png)

# In[ ]:


# [1] 코드 작성
def func(x):
    return x.max() - x.min()
    
df.groupby('업종명')[['종가','시가','거래대금']].apply(func)
#df.groupby('업종명')[['종가','시가','거래대금']].agg(func)
#df.pivot_table(index='업종명', values=['종가','시가', '거래대금'], aggfunc=func)


# ## [2] df에서 업종별 컬럼마다 다른 함수로 집계하라
# ### 업종별 '거래대금'은 max와 min집계, '시가'는 min집계, '종가'는 max집계 한다
# - 다음 결과를 참고하라
# ![image-2.png](attachment:image-2.png)

# In[ ]:


# [2] 코드 작성
df.groupby('업종명').agg({'거래대금':['max','min'], '시가':'min', '종가':'max'})


# ## [3] df에서 업종별 최고 거래량으로 개별집계하라
# ### 업종별 거래량으로 max집계하여 개별 집계로 원본 형태로 구성하여 '최고거래량'컬럼을 추가하라
# - 다음 결과를 참고하라
# ![image-4.png](attachment:image-4.png)

# In[ ]:


# [3] 코드 작성
df['최고거래량'] = df.groupby('업종명')['거래량'].transform('max')
df


# ## [4] df에서 업종별로 등락률의 최저값이 +인 업종의 해당 종목들을 추출하라
# - sr는 업종별 등락률의 최저값을 집계한 결과로 등락률의 최저값이 오른(+) 업종은 전기전자이다
# - 전기전자업종의 해당 종목을 인쇄한 다음 결과를 참고하라
# 
# ![image-8.png](attachment:image-8.png)

# In[ ]:


sr = df.groupby('업종명')['등락률'].min() # 업종별 등락률의 최저값(확인용)
sr

# [4] 코드 작성
def func(x):
    return x['등락률'].min()>0

df.groupby('업종명').filter(func)

