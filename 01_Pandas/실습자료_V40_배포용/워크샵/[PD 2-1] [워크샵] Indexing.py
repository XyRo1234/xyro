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


# # [ 인구조사 데이터셋 ]
# ### 수원시 2022년 1월 연령별 인구현황 데이터셋을 이용하여 다음 조건들을 처리한다
# - 원본 'suwon_census_원본.csv'와 편집한 'suwon_census.csv'파일이 주어진다
# - 지역은 수원시, 기간은 2022년 1월, 연령구분단위는 1세단위로 선택한 자료이다
# - 데이터셋 참고 사이트 : 행정안전부사이트 https://jumin.mois.go.kr 
# ![image-5.png](attachment:image-5.png)

# ## [0]  파일 내용 확인하기
# ### 1. 다운받은 원본 'suwon_census_원본.csv'파일을  실행하여 사전에 편집해야 할것들을 살펴보자
# - 행정구역을 도,시,구,동으로 분리
# - 컬럼명에서 나이만 추출
# - 불필요한 행, 컬럼을 삭제
# - 세자리마다 콤마 제거하고 정수타입으로 변환
# - 이러한 편집에 대한 내용은 추후 학습함
# 
# ### 2. 원본을 편집한 'suwon_census.csv'파일을 실행하여 편집 전후의 내용을 확인하라
# - 행 정보 : 44개 행정구역을 갖는 44개 행으로 구성되어 있다
# - 컬럼 정보 : 행정명칭 도/시/구/동 4개와 '0세' ~ '100세 이상'까지 101개 연령으로 구성되어 있다
# 
# ![image-8.png](attachment:image-8.png)

# In[2]:


# df = pd.read_csv('suwon_census_원본.csv', encoding = 'ANSI') # 원본 파일
df = pd.read_csv('suwon_census.csv') # 편집한 파일
df.info()
df


# ## [1] 컬럼 인덱싱 1
# ### '100세 이상'인 컬럼에서 최고령 인구가 가장 많은 5개 지역을 추출한 후  '동'과 '100세 이상'컬럼만 인덱싱하여 인쇄하라(다음 그림 참조)
#   
# ![image-7.png](attachment:image-7.png)

# In[3]:


# [1] 코드 작성
df.nlargest(5, '100세 이상')[['동','100세 이상']]


# ## [2] 컬럼 인덱싱 2
# ### 20대 컬럼만 추출하고 앞에서 5개행만 인덱싱하여 인쇄하라(다음 그림 참조) 
# ![image-3.png](attachment:image-3.png)  

# In[4]:


# [2] 코드 작성
# df.iloc[0:5,24:34]
df.loc[0:4, '20세':'29세']


# ## [3] 컬럼 추가
# ### 3-1. 연령이 20대(20 ~ 29세)인 컬럼들만 추출하여 ndf에 대입하라
# ### 3-2. 생성한 ndf 데이터프레임의 마지막 컬럼에 '동' 컬럼을 추가하여 인쇄하라
# 다음 그림은 ndf의 일부만 인쇄한 결과이다
# ![image-5.png](attachment:image-5.png)

# In[5]:


# [3-1] 코드 작성
ndf = df.iloc[:,24:34]

# [3-2] 코드 작성
ndf['동'] = df['동']
ndf


# ## [4] 컬럼 인덱싱 3
# ### df 컬럼에서 0세, 10세, 20세, ... 100세 이상 순서번째만 컬럼을 추출하여 인쇄하라
# - 다음은 일부만 인쇄한 결과이다
# ![image-3.png](attachment:image-3.png)

# In[6]:


# [4] 코드 작성
df.loc[:,'0세':'100세 이상']



# ## [5] 행과 컬럼 인덱싱
# ### 주어진 df2는 '동'컬럼을 index로 'suwon_census.cvs' 파일을 읽어온 데이터이다(다음 그림참조)
# ![image-11.png](attachment:image-11.png)
# 
# ### 5-1. df2에서 '율천동'지역 10세 미만 데이터들로 구성한 Series를 인쇄하라(다음 그림 참조)
# ![image-8.png](attachment:image-8.png)

# In[7]:


df2 = pd.read_csv('suwon_census.csv', index_col='동')
df2.head(2)

# [5-1] 코드 작성
sr2 = df2.loc['율천동','0세':'9세']
print(sr2)


# ### 5-2. df2에서 '장안구'지역으로 '파장동'에서 '연무동'까지 20대 연령 데이터만 인쇄하라(다음그림 참조)
# ![image-10.png](attachment:image-10.png)

# In[6]:


df2 = pd.read_csv('suwon_census.csv', index_col='동')
df2.head()

# [5-2] 코드 작성
df2.loc['파장동':'연무동','20세':'29세']


# ## [6] line차트로 시각화하는 다음 코드를 이해하라
# ### * 판다스에서는 plot()메서드를 이용하여 간편하게 시각화한다
# - plot메서드는 matplotlib 모듈을 이용하여 시각화한다  
# - plot()의 옵션
#     - figsize=(너비, 높이) : 챠트 크기를 지정하는 옵션으로 인치 단위  
#     - xticks=sequence : x축상의 위치 표시 지점에 label을 직접 지정    
#     - tick이란? 축상의 위치 표시 지점을 틱(tick)이라고 하고 이 틱에 써진 숫자 혹은 글자를 틱 레이블(tick label)이라고 한다. 틱의 위치나 틱 레이블은 자동으로 정해진다   
#     
# ### 6-1. 인계동의 인구현황을 line 차트로 시각화하는 다음 코드를 이해하라
# - sr.plot() ==> sr의 index가 x축, values가 y축에 line챠트로 시각화한다    

# In[8]:


# [6-1] 코드 이해

df2 = pd.read_csv('suwon_census.csv', index_col='동')
sr = df2.loc['인계동', '0세':]
sr

sr.plot(figsize=(15,5))


# ### 6-2. x축 tick을 10살 단위로 조정한 다음 코드를 실행하라

# In[13]:


# [6-2] 코드 이해

sr.plot(figsize=(15, 5), xticks=range(0,101,10))


# ## [7] 입력받은 특정 지역의 인구현황을  line 챠트로 시각화하라
# - 다음 그림은 지역명을 입력받아 시각화한 결과이다 
# ![image-5.png](attachment:image-5.png)   
# 
# ### 7-1. 지역명(동)을 dong 변수에 입력 받는다

# In[14]:


# [7-1] 코드 실행

df2 = pd.read_csv('suwon_census.csv', index_col='동')
print('* 지역 목록 ==>', df2.index.to_list())
dong = input('* 지역명(동)을 입력하시오==>')


# ### 7-2. df2에서 입력받은 해당동(dong)의 전연령을 인덱싱하여 sr 변수에 대입하라
# ### 7-3. sr를 이용하여 line 챠트로 시각화하라. 단, xtick을 10단위로 조정한다

# In[17]:


# [7-2] 코드 작성
sr = df2.loc[dong,'0세':'100세 이상']
sr
# [7-3] 시각화
sr.plot(figsize=(15, 5), xticks=range(0,101,10))

