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
mpl.rc('font', size=16) # 전체 폰트크기 지정


# # < 2021년도 대비 2022년도 인구변화 비교 >
# ## [0] 파일에서 읽어온 df1, df2 실행하여 확인하기
# ### 2021년 1월, 2022년 1월 인구조사 데이터셋으로 작년대비 남녀별 인구변화를 비교분석하려 한다

# In[2]:


col1 = ['시','구','동','21_총계','21_세대수','21_남자','21_여자']
col2 = ['시','구','동','22_총계','22_세대수','22_남자','22_여자']

df1 = pd.read_csv('suwon_census_202101.csv',header=0, names=col1, index_col='동')
df1.head(2)
df2 = pd.read_csv('suwon_census_202201.csv',header=0, names=col2, index_col='동')
df2.head(2)


# ## [1] 컬럼 추가
# ### df1(2021년도)에서 남녀 2개 컬럼을 df2의 '구'컬럼 뒤에 추가하라
# - 추가할 컬럼명은 '21_남자', '21_여자'컬럼순으로 추가하여 배치한다(다음 그림 참고(일부))  
# ![image-7.png](attachment:image-7.png)

# In[3]:


# [1] 코드 작성
# df1.loc[:,['21_남자','21_여자']]
df2.insert(2, '21_남자', df1['21_남자'])
df2.insert(3, '21_여자', df1['21_여자'])
df2


# ## [2] 컬럼 삭제
# ### df2에서 '시', '구', '22_총계', '22_세대수' 컬럼을 df2 원본에서 삭제하라
# - 다음 그림을 참고(일부)
# ![image-4.png](attachment:image-4.png)

# In[4]:


# 삭제할 컬럼 label 
col = ['시', '구', '22_총계', '22_세대수']

# [2] 코드 작성
df2.drop(columns=col, inplace=True)
df2


# ## [3] 다중 컬럼 추가
# ### [2]번 문제에서 완성한 df2를 이용하여 2022년도와 2021년도 남녀별 편차를 구하여 컬럼을 추가하라
# - 아래 그림을 참고(일부)하여 'man_dev', 'woman_dev' 2개의 컬럼을 추가하라
# - man_dev = 22_남자 - 21_남자
# - woman_dev = 22_여자 - 21_여자
# 
# ![image-5.png](attachment:image-5.png)

# In[5]:


# [3] 코드 작성
df2 = df2.assign(man_dev=df2['22_남자'] - df2['21_남자'],  woman_dev=df2['22_여자'] - df2['21_여자'])
df2


# ## [4] 데이터프레임 update
# ### 주어진 udf(2021년 7월데이터)로 df2의 21년도 남녀인구수를 update하라 
# - udf는 2021년도 7월 인구데이터 'suwon_census_202107.csv'파일을 읽어온 데이터프레임이다
# - 2021년도 1월 데이터를 2021년도 7월달 데이터로 남녀인구수를 update하려 한다
# - 남녀 인구수 편차를 재계산하는 df2.assign()코드가 주어져 있다
# ![image-7.png](attachment:image-7.png)

# In[6]:


# udf(2021년도 7월) 
col1 = ['시','구','동','21_총계','21_세대수','21_남자','21_여자']
udf = pd.read_csv('suwon_census_202107.csv',header=0, names=col1, index_col='동')
udf.head()

# [4] 코드 작성
df2.update(udf.loc[:,['21_남자','21_여자']])


# update 후 남녀 인구 편차 재계산
df2 = df2.assign(man_dev=df2['22_남자']-df2['21_남자'],\
                 woman_dev=df2['22_여자']-df2['21_여자'])
df2.head()


# ## [5] 데이터프레임 재구성
# ### 다은 조건에 따라 순서대로 처리하여 ndf에 대입하라
# 1. df2에서 남성 편차(man_dev)가 가장 높은 순으로 5개 행을 추출한다.
# 2. col변수를 이용하여 남성 정보 컬럼만 추출한다.
# 3. 동 index를 컬럼으로 이동시킨다.
# 4. 행의 index를 '1위'부터 순서대로 부여한다.
# - 완성된 다음 그림을 참고하여 재구성하라
# ![image-2.png](attachment:image-2.png)

# In[7]:


col = ['21_남자', '22_남자', 'man_dev']

# [5] 코드 작성
ndf = df2.nlargest(5, columns = 'man_dev')
ndf = ndf.loc[:,col]
ndf.reset_index('동', inplace=True)
ndf.rename(index=lambda x : str(x+1)+'위', inplace=True)
ndf

