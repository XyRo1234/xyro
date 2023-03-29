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
mpl.rc('font',size=16) # 전체 폰트 지정


# # << 타이타닉 데이터 >>
# ## [0] titanic_train.csv 파일을 확인하라
# - 타이타닉 호 침몰 당시의 승객 명단 데이터로 생존자의 생사여부와 다른 데이터들 간의 연관성을 분석하여 생존에 영향을 미치는 요소를 비교 분석용도로 사용되는 데이터 셋이다
# - titanic 데이터는 캐글 사이트(https://www.kaggle.com/c/titanic/data)   에서 'train.csv'파일을 다운로드 받을 수 있다
# - 컬럼 의미   
# Survived: 생존 여부  
# pclass: 티켓 등급   
# Name : 이름   
# Sex: 성별  
# Age: 나이  
# Sibsp: 함께 탑승한 형제자매, 배우자의 수  
# Parch: 함께 탑승한 부모, 자식의 수  
# Ticket: 티켓 번호  
# Fare: 운임  
# Cabin: 객실 번호  
# Embarked: 탑승 항구( C = Cherbourg, Q = Queenstown, S = Southampton)  

# In[2]:


df_tit = pd.read_csv('titanic_train.csv')
df_tit.info()
df_tit.head(2)


# ### 실습에 사용할 df를 확인하라
# - df_tit에서 생존여부, 선실등급, 이름, 성별, 나이 5개의 컬럼만 가져온 df이다
# - describe()로 수치형 컬럼의 분포도를 확인한다

# In[3]:


df = df_tit.iloc[:, [1,2,3,4,5] ]
df.describe()
df.head()


# ## [1] 60세 이상 생존자의 정보를 행단위로 추출하라
# - 생존자의 경우는 Survived 컬럼의 값이 1이다(다음 그림 참고)   
# ![image-4.png](attachment:image-4.png)

# In[5]:


# [1] 코드 작성
df[ (df['Survived']==1) & (df['Age']>=60) ]


# ## [2] 나이가 20대인 인원수를 구하라
# - 20 ~ 29세 사이의 인원수는 220명이다

# In[30]:


# [2] 코드 작성
# df[ (20 <= df['Age'] < 30) ].count()
df.loc[ (df['Age']>=20) & (df['Age'] < 30) , 'Age'].count()


# ## [3] 'Name'에서 호칭이 'Miss'인 여성중 생존자의 인원수를 인쇄하라
# - 결과는 127이 인쇄되어야 한다

# In[31]:


# [3] 코드 작성
df.loc[df['Name'].str.contains('Miss') & df['Survived']==1, 'Name'].count()


# ## [4] 연령대를 아동과 성인으로 구분하여 생존자수 비교하라
# 1. 18세미만과 이상으로 'child'과 'adult'로 구분하여 'Age2'컬럼을 추가하라
# 2. 생존자중에서 'Age2'컬럼으로 인원 빈도 집계한다
# - 다음 그림 참고(Age2추가된 결과는 일부임)
# ![image-5.png](attachment:image-5.png)
# - 참고) 인덱싱방법으로 수정시 SettingWithCopyWarning이 발생할 경우
#     pd.set_option('mode.chained_assignment',  None) 로 경고를 끈다

# In[24]:


# 편집시 경고발생할 경우 해제 방법 
pd.set_option('mode.chained_assignment',  None) # 경고 끔


# In[32]:


# [4] 코드 작성
df.loc[df['Age']>=18, 'Age2'] = 'adult'
df.loc[df['Age']<18, 'Age2'] = 'child'
df
df.loc[df['Survived']==1, 'Age2'].value_counts()


# ## [5] 나이 정보가 누락된 사람들의 선실 및 성별 분포도를 확인하라
# ###  df의 'Age' 컬럼에서 누락된 자료만 추출하여 선실(Pclass) 및 성별(Sex) 인원 집계하라
# - 다음 그림을 참고(일부)
# ![image-4.png](attachment:image-4.png)
# ![image-10.png](attachment:image-10.png)

# In[59]:


# [5] 코드 작성
df.loc[df['Age'].isna() ,['Pclass','Sex']].value_counts()
# df.loc[df['Age'].isna() ,['Pclass','Sex']].count()
# df.loc[df['Age'].isna() ,['Pclass','Sex']]


# In[ ]:




