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


# # << 전국 월별 아파트거래 데이터 전처리>>
# ## [0] '아파트거래_월별2.xlsx' 파일 파악하기
# ### 전처리 할 내역들
# 1. 변경 전 주소나 신도시인 경우 빈란에 '-'로 표기되어 대부분 object타입으로 읽어와 '-'은 모두 누락처리하여 수치형 데이터로 변경해야 한다
# 2. 아래 그림처럼 지역1, 지역2의 빈칸엔 해당 도나 시명칭으로 채워넣어야 한다
# 3. 수원시 행정명칭을 수원특례시로 변경해야 한다
# 4. 지역2와 지역3 컬럼을 하나의 주소로 합치는 편집이 필요하다. 
# 5. 컬럼명의 년월표기명을 약식으로 편집이 필요하다.
# 6. 최종 완성된 df을 파일로 저장한다
# ![image-5.png](attachment:image-5.png)

# In[2]:


# [0] 파일 확인
df_apt = pd.read_excel('아파트거래_월별2.xlsx', header=10)
df_apt.info()
df_apt


# ## [1] df_apt에서 '-'를 누락처리하여 df변수에 대입하라
# - 파일을 다시 읽어오거나 재편집하는 다양한 방법이 있다. 처리후 컬럼의 타입을 확인하라
# - 다음 그림 참고(일부)
# ![image-5.png](attachment:image-5.png)

# In[3]:


# [1] 코드 작성
df = df_apt.replace('-', np.nan)
df.info()
df.head(6)


# ## [2]  df에서 '지역1'과  '지역2' 컬럼내 빈칸 채우기
# ### 예로 지역1 컬럼내 최초의 '서울' 뒤에 결측값을 '서울'값으로, 지역2 컬럼내 수원시도 뒤에 결측치를 수원시로 채운다
# - 참고) fillna의 method방식에서 0축 방향, 전방값으로 채우기를 이용한다
# ![image-6.png](attachment:image-6.png)

# In[4]:


# [2] 코드 작성
df.loc[:,'지역1':'지역2'] = df.loc[:,'지역1':'지역2'].fillna(method='ffill')



# 확인
df.head() # 서울 일부
df.loc[85:91] # 수원 일부


# ## [3] df에서 '지역2'컬럼내 '수원시'를 '수원특례시'로 변경하라
# - 원본 df를 수정한다. 다음 그림 참고(일부)
# ![image-2.png](attachment:image-2.png)

# In[5]:


# [3] 코드 구현
df = df.replace({'지역2':{'수원시':'수원특례시'}})

# 확인
df.loc[85:91] # 수원 일부


# ## [4] df에서 '지역2'와 '지역3' 컬럼 합치기
# ### 지역2와 지역3을 합쳐 '지역2'컬럼에 갱신하고 '지역3'컬럼은 삭제한다
# - 문자열과 문자열은 덧셈('+') 연산으로 연결할수 있다. 단 결측치값은 연산이 안된다. 즉 결측치를 빈문자열('')로 대체후 연산한다
# - 다음 그림 참고(일부)
# ![image-7.png](attachment:image-7.png)

# In[6]:


# [4] 코드 작성
df['지역2'] = df['지역2'] + df['지역3'].fillna('')
df.pop('지역3')
# 확인
df.head() # 서울 일부
df.loc[85:90] # 수원 일부


# ## [5] df의 컬럼명 편집하기
# ### 날짜로 구성된 컬럼명만 예로 '2022년 05월'을 '22_05'로 편집한다
# - 다음 그림 참고(일부)
# ![image-3.png](attachment:image-3.png)

# In[7]:


# [5] 코드 작성
def func(x):
    return x[2:4] + '_' + x[6:8] if x[0]=='2' else x

df.rename(columns = func, inplace = True)
df


# ## [6] 완성한 df을 newfile('apart_sale.xlsx') 파일로 저장하고 df2로 읽어오기
# - 파일로 저장하고 df2 변수로 읽어온 후 인쇄하여 파일 내용을 확인하라

# In[8]:


newfile ='apart_sale.xlsx'

# [6] 코드 작성
df.to_excel(newfile, index=False)
df2 = pd.read_excel(newfile)
df2


# ## [7] 인천의 2022년도 11월 매매현황을 pie챠트로 시각화
# ### 7-1. df2에서 인천의 '22_11'컬럼의 매매량을 추출하여 sr에 대입하라
# - '총계'와 결측치(남구지역)지역은 제외한다. 결과 Series는 다음과 같다
# ![image.png](attachment:image.png)

# In[9]:


# [7-1] 코드 작성
sr = df2.set_index(['지역1','지역2']).loc['인천', '22_11'][1:].dropna()
sr


# ### 7-2. 완성한 sr로 pie챠트 그리는 다음 코드를 실행하여 확인하라
# - pie 챠트의  wedgeprops옵션 이해
#     - 예로 wedgeprops={'width': 0.5, 'edgecolor': 'w', 'linewidth': 5} 
#     - width : 부채꼴 영역의 너비(반지름에 대한 비율), edgecolor : 테두리의 색상, linewidth : 테두리 선의 너비 

# In[11]:


# [7-2] 코드 실행 : pie 차트로 시각화

wedgeprops={'width': 0.5, 'edgecolor': 'w', 'linewidth': 5} 
sr.plot(kind='pie', figsize=(9,9), autopct='%.1f%%', wedgeprops=wedgeprops);


# In[ ]:




