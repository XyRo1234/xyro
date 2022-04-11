import os
import re
import pandas as pd



Astep_path = "D:\\영상콘텐츠\\냉장고\\언어Vari_220120"
Astep_path2 = "D:\\영상콘텐츠\\냉장고\\언어Vari_220216_2차"

from collections import OrderedDict                                                           # OrderedDict Import하기
friend_ordered_dict = OrderedDict([('Episode',['E01','E02','E03','E04','E05','E06','E07','E08','E09','E10','E11','E12','E13','E14','E15','E16','E17','E18','E19','E20','E21']) ]) # OrderedDict 사용해서 data를 저장. column fixed(data순서) 시킴
df = pd.DataFrame.from_dict(friend_ordered_dict)                                              # DataFrame 생성.(.from_dict) 사용
# print(df)
c_header = []
Astep_filenames = os.listdir(Astep_path)
Astep_filenames2 = os.listdir(Astep_path2)
p = re.compile("..-[a-zA-Z]{2}")
e = re.compile("E\d{2}")

Bstep_paths = []
for a in Astep_filenames:
    if p.search(a) and '.' not in a:    # [ar-AE]와 같은 국가코드가 있고, 폴더(".""없는) 이면, 
        Bstep_path = (f"{Astep_path}\\{a}")
        Bstep_paths.append(Bstep_path)
        # Bstep_filenames = os.listdir(Bstep_path)


Bstep_paths2 = []
for a in Astep_filenames2:
    if p.search(a) and '.' not in a:    # [ar-AE]와 같은 국가코드가 있고, 폴더(".""없는) 이면, 
        Bstep_path2 = (f"{Astep_path2}\\{a}")
        Bstep_paths2.append(Bstep_path2)

cycle = []
for a in Astep_filenames2:
    if p.search(a) and '.' not in a:
        cycle.append(a)


for a in cycle:
    w = ''
    ox_check = []
    arAE = p.search(a).group()
    for Bstep_path in Bstep_paths:
        if arAE in Bstep_path:
            Bstep_filenames = os.listdir(Bstep_path)
            for a in Bstep_filenames:
                w = w + " " + str(a)
    for Bstep_path2 in Bstep_paths2:
        if arAE in Bstep_path2:
            Bstep_filenames = os.listdir(Bstep_path2)
            for a in Bstep_filenames:
                w = w + " " + str(a)

    for n in range(1,10):
        if f"E0{n}" in w:
            ox_check.append("O")
        else:
            ox_check.append("X")

    for n in range(0,10):
        if f"E1{n}" in w:
            ox_check.append("O")
        else:
            ox_check.append("X")

    for n in range(0,2):
        if f"E2{n}" in w:
            ox_check.append("O")
        else:
            ox_check.append("X")
    # print(p.search(a).group() ,": " ,ox_check)
    df[p.search(a).group()] = ox_check

print(df.head())
df.to_csv('friend_list_from_df.csv')




# for a in Astep_filenames:
#     if p.search(a) and '.' not in a:    # [ar-AE]와 같은 국가코드가 있고, 폴더(".""없는) 이면, 
#         Bstep_path = (f"{Astep_path}\\{a}")
#         Bstep_filenames = os.listdir(Bstep_path)

#         c_header.append(p.search(a).group())        # df해더생성
#         ox_check = []
#         w = ''
#         for a in Bstep_filenames:
#             w = w + " " + str(a)
#         if "E01" in w:
#             ox_check.append("O")
#         else:
#             ox_check.append("X")
#         if "E02" in w:
#             ox_check.append("O")
#         else:
#             ox_check.append("X")
#         print(p.search(a).group() ,": " ,ox_check)
#         df[p.search(a).group()] = ox_check
# print(df.head())



# p = re.compile("..-[a-zA-Z]{2}")
# m = p.search(path)
# wsname = m.group()