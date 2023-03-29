# x = eval(input())
# print(x)

import pandas as pd
import numpy as np




# from IPython.core.interactiveshell import InteractiveShell
# InteractiveShell.ast_node_interactivity = "all"

# [0]

import pandas as pd 
import numpy as np

# 채점시스템 제출시는 test변수를 1로 수정하여 제출하세요 #
# 0: 파일에서 데이터 로드, 1: 채점시스템에서 로드

test = 1

if test == 1 :
    t = eval(input())
    df = pd.DataFrame(t[1:], columns = t[0]).iloc[:, [0,1,2,3,4,7]]
else :
    df = pd.read_csv('titanic_train.csv', usecols=[1,2,3,4,5,8])

df.head(6)


# [문제 1]

#--[아래에 코드 작성]--------------------------------------------------
df.insert(0,'Last',df['Name'].apply(lambda x : x.split(',')[0]))
r1 = df['Last'].head(10)

#--[검증용코드, 수정금지]--------------------------------------------------
df.head()
print(r1)


# [문제 2]

#--[아래에 코드 작성]--------------------------------------------------
sr2 = df.groupby(['Last','Ticket']).size()
r2 = sr2.head(10)
#--[검증용코드, 수정금지]--------------------------------------------------
sr2
print(r2)


# [문제 3]

#--[아래에 코드 작성]--------------------------------------------------
df3 = sr2.reset_index()
df3 = df3.rename({0:'cnt'},axis=1)
r3 = df3['cnt'].head(10)

#--[검증용코드, 수정금지]--------------------------------------------------
df3
print(r3)


# [문제 4]

#--[아래에 코드 작성]--------------------------------------------------
df4 = df3[df3['cnt']>=2].reset_index(drop=True)
r4 = df4['cnt'].head(10)
#--[검증용코드, 수정금지]--------------------------------------------------
df4
print(r4)


# [5번 문제] 

#--[아래에 코드 작성]--------------------------------------------------
df5 = df4.merge(df, how='left')
r5 = df5['Pclass'].head(10)
#--[검증용코드, 수정금지]--------------------------------------------------
df5
print(r5)


# [6번 문제] 

#--[아래에 코드 작성]--------------------------------------------------
r6 = df5.groupby('cnt').agg(sum = ('Name','size'), alive=('Survived','sum'))
#--[검증용코드, 수정금지]--------------------------------------------------
r6
print(r6)


# [7번 문제] 

#--[아래에 코드 작성]--------------------------------------------------
# df4.head()
m = df4['Last'].duplicated(keep=False)
df7 = df4[m]

df8 = df7.merge(df, how='left')

# def f1(x):
#     return x['Survived'].sum() == 0
# r7 = df8.groupby(['Last','Ticket']).filter(f1).reset_index()['Name']
r7 = df8.groupby(['Last','Ticket']).filter(lambda x : x['Survived'].sum()==0).reset_index()['Name']

#--[검증용코드, 수정금지]--------------------------------------------------
df7
df8
print(r7)





