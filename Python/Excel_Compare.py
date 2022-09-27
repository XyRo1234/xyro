import openpyxl
import pandas
import numpy as np

x=np.array(['TA','B','C'])
print(x)
x[0]='A'
print(x)
print("차원 : ", x.ndim)
print("행수,열수 : ", x.shape)
#print(x.ndim)     #몇차원인지 확인
#print(x.shape)    #배열의 모양 확인 (행수,열수)
# np.insert(Array_Name,Index_No,Value)

print("\n")
"""
:2  0부터 2미만, 0,1
:   처음부터 끝까지
1:  1부터 끝까지
"""
arr3 = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(arr3)
print(arr3[0])
arr3[:2, 1:]            # [Column(열), Row(행)]
print("\n")
print(arr3[:2, 1:])
print("\n")

names = np.array(['kim','lee','park','choi','will','kim','park','kim'])
names == 'kim'
print(names)
