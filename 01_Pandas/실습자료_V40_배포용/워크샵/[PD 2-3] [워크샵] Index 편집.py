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
mpl.rc('font',size=16) # 전체 폰트크기 지정


# ## [0]  suwon_census2.csv 파일 확인하기
# 2022년도 1월의 수원시 연령별 인구조사 데이터이다. 다음 코드를 실행하여 확인하라

# In[2]:


df = pd.read_csv('suwon_census2.csv')
df.info()
df.head(2)


# ## [1] 컬럼명 편집
# ### 컬럼명을 년도와 월을 제거하여 나이로만 편집하라
# - rename()을 이용하며 split('_')로 구분하여 마지막 단어인 나이만 선택한다
# - 반드시 원본이 수정되도록 inplace 키워드를 이용한다
# - 다음 그림을 참조하여 편집한 결과를 인쇄하라(인쇄결과는 일부임)
# 
# ![image-3.png](attachment:image-3.png)

# In[3]:


# [1] 코드 작성
df.rename(columns=lambda x : x.split('_')[-1], inplace=True)
df


# ## [2] index 편집 1
# ### 2-1. df에서 '구'와 '동'컬럼을 multiIndex화하여 ndf에 대입하라(아래 그림 참고)
# ![image-17.png](attachment:image-17.png)

# In[4]:


# [2-1] 코드 작성
ndf = df.set_index(['구','동'])
ndf


# ### 2-2. 완성한 ndf를 이용하여 '장안구'를 인덱싱하여 인쇄하라
# - (참고) 멀티인덱스에서 0 level('구')을 선택하면 장안구 1 level의 모든 동이 추출된다
# - 아래 그림은 '장안구'를 인덱싱한 결과 일부이다
# ![image-18.png](attachment:image-18.png)

# In[5]:


# [2-2] 코드 작성
ndf.loc['장안구']


# ## [3] index 편집 2
# ### 다음조건에 따라 순서대로 처리하여 ndf에 대입하여 인쇄하라
# 1. df에서 '구' 컬럼을 index화하고 '장안구' 데이터만 추출한다
# 2. 추출한 데이터프레임에서 index를 0부터 일련번호로 초기화하여 인쇄하라
# - (참고) index의 label은 중복이 가능하므로 중복된 '장안구' label이 모두 인덱싱 대상이 된다
# - 다음 그림은 ndf의 인쇄 결과 일부이다
# ![image-9.png](attachment:image-9.png) ![image-10.png](attachment:image-10.png)

# In[6]:


# [3] 코드 작성
ndf = df.set_index('구').loc['장안구'].reset_index(drop=True)
ndf


# ## [4] 정렬
# ### df에서 '구'와 '동' 컬럼을 기준으로 오름차순 정렬하여 인쇄하라
# - 다음 그림은 정렬한 결과의 일부이다   
# ![image-2.png](attachment:image-2.png)

# In[7]:


# [4] 코드 작성
df.sort_values(['구','동'])


# ## [5] 데이터 회전
# ### 다음 조건을 순서대로 구현하여 ndf에 대입하고 인쇄하라
# 1. df에서 '동' 컬럼을 index화한다
# 2. '행궁동'과 '인계동' 2개 행과 나이 컬럼들('0세' ~ '100세이상')을 인덱싱한다
# 3. 행과 열을 회전하여 재구성한 결과를 ndf에 대입하고 인쇄하라(다음 그림 참조(일부))
# ![image-3.png](attachment:image-3.png)

# In[8]:


# [5] 코드 작성
ndf = df.set_index('동').loc[['행궁동','인계동'],'0세':].T
ndf


# ## [6] line차트 시각화 예시
# ### 위 [5]번문제에서 완성한 ndf를 이용하여 행궁동과 인계동의 인구분포도를 시각화하는 다음 코드를 이해하라
# - plot() 옵션
#     - style : 점, 라인, 색상을 지정한다. 순서 무관하게 서로 조합하여 '--b'와 같은 문자열로 지정 
#         - marker(점모양) : .(point), o(circle), v, ^, < , >, s, *, X, +등등
#         - line모양 : -, --, :, -. 
#         - color : b, g, r, x, m , k(black), w
#     - xlabel, ylabel : 축 제목 지정

# In[9]:


# [6] 코드 이해
ndf = df.set_index('동').loc[['행궁동','인계동'], '0세':].T

# line style, y축제목(ylabel), xtick 지정하여 꾸미기
ndf.plot(figsize=(15,5), style=['-.r', '--g'], ylabel='인구수', xticks=range(0,101,10))


# ## [7]특정지역의 20대 연령층만 line차트 시각화
# ### 7-1. df에서 ['동']을 index화하고 주어진 3개지역(col변수)의 20대 연령만 추출하여 행과 열을 회전한 데이터프레임을 ndf변수에 대입하라
# - 다음 그림은 완성된 ndf이다
# ![image-6.png](attachment:image-6.png)

# In[13]:


col = ['영통1동','영통2동','영통3동']

# [7-1] 코드 작성
ndf = df.set_index('동').loc[col,'20세':'29세'].T
ndf


# ### 7-2. 주어진 style변수를 이용하여 ndf을 line 차트로 시각화하라
# 다음 그림은 영통 3개 지역의 20대 연령의 분포도를 line 차트로 시각화한 결과이다
# ![image-7.png](attachment:image-7.png)

# In[17]:


style = ['^:r', 'o--m', 's-.g']

# [7-2] 코드 작성
ndf.plot(figsize=(15,5), style=style, xticks=range(0,10,1))

