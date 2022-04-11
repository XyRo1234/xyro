import os
import re
import shutil

# path4 = "D:\\9_TM\ExportFiles\\REF_en-GB_번역결과_0127"
# path3 = "D:\영상콘텐츠\냉장고\언어Vari_220216_2차"

# """ 파일복사붙여넣기 """
# path_file_list = []         # srt, ssml, 2D text 모두 경로+파일명 리스트로 만들기
# for (path, dir, files) in os.walk(path4):
#     for a in dir:
#         path_file_list.append(path + '\\' + a)

# path_file_list2 = []        # 복사한 폴더를 넣을 위치 리스트로 만들기
# path_file_list2 = os.listdir(path3)
# # for (path, dir, files) in os.walk(path3):
# #     for a in dir:
# #         path_file_list2.append(path + '\\' + a)

# for a in path_file_list2:
#     try:
#         p = re.compile("..-[a-zA-Z]{2}")
#         m = p.search(a).group()
#         old_path1 = f"D:\\9_TM\\ExportFiles\\REF_en-GB_번역결과_0127\\{m}\\UK_1"    # 복사할 위치
#         old_path3 = f"D:\\9_TM\\ExportFiles\\REF_en-GB_번역결과_0127\\{m}\\UK_3"    # 복사할 위치
#         new_path1 = f"D:\\영상콘텐츠\\냉장고\\언어Vari_220216_2차\\{m}_LG_RF_How_To_Video_220216\\UK_1" # 붙여넣을 위치
#         new_path3 = f"D:\\영상콘텐츠\\냉장고\\언어Vari_220216_2차\\{m}_LG_RF_How_To_Video_220216\\UK_3" # 붙여넣을 위치

#         if not os.path.exists(new_path1):
#             shutil.copytree(old_path1, new_path1)
#         if not os.path.exists(new_path3):
#             shutil.copytree(old_path3, new_path3)
#     except:
#         pass


# """ 다국어srt파일 path+filename으로 리스트만들기 """
# AC_list = []    # AC: All Countries
# for (CC_path, dir, files) in os.walk(path3):
#     for a in dir:
#         try:
#             if "UK_1" in a:
#                 os.rename(CC_path+"\\"+"UK_1", CC_path+"\\"+"1__subtitles")
#             elif "UK_3" in a:
#                 os.rename(CC_path+"\\"+"UK_3", CC_path+"\\"+"3__2Dtext")
#         except FileExistsError:
#             print("해당폴더명이 존재합니다.")
#             shutil.rmtree(CC_path+"\\"+"1__subtitles")  # 폴더삭제
#             shutil.rmtree(CC_path+"\\"+"3__2Dtext")  # 폴더삭제
#             if "UK_1" in a:
#                 os.rename(CC_path+"\\"+"UK_1", CC_path+"\\"+"1__subtitles")
#             elif "UK_3" in a:
#                 os.rename(CC_path+"\\"+"UK_3", CC_path+"\\"+"3__2Dtext")


path4 = "D:\\영상콘텐츠\\세탁기\\번역문"
path3 = "D:\\영상콘텐츠\\세탁기\\언어Vari_220221_2차"

""" 파일복사붙여넣기 """
path_file_list = []         # srt, ssml, 2D text 모두 경로+파일명 리스트로 만들기
for (path, dir, files) in os.walk(path4):
    for a in dir:
        path_file_list.append(path + '\\' + a)

path_file_list2 = []        # 복사한 폴더를 넣을 위치 리스트로 만들기
path_file_list2 = os.listdir(path3)
# for (path, dir, files) in os.walk(path3):
#     for a in dir:
#         path_file_list2.append(path + '\\' + a)

for a in path_file_list2:
    try:
        p = re.compile("..-[a-zA-Z]{2}")
        m = p.search(a).group()
        old_path1 = f"{path4}\\{m}\\1__srt"    # 복사할 위치
        old_path3 = f"{path4}\\{m}\\3__excel"    # 복사할 위치
        new_path1 = f"{path3}\\{m}_LG_WM_How_To_Video_220216\\1__srt" # 붙여넣을 위치
        new_path3 = f"{path3}\\{m}_LG_WM_How_To_Video_220216\\3__excel" # 붙여넣을 위치

        if not os.path.exists(new_path1):
            shutil.copytree(old_path1, new_path1)
        if not os.path.exists(new_path3):
            shutil.copytree(old_path3, new_path3)
    except:
        pass


""" 다국어srt파일 path+filename으로 리스트만들기 """
AC_list = []    # AC: All Countries
for (CC_path, dir, files) in os.walk(path3):
    for a in dir:
        try:
            if "1__srt" in a:
                os.rename(CC_path+"\\"+"1__srt", CC_path+"\\"+"1__subtitles")
            elif "3__excel" in a:
                os.rename(CC_path+"\\"+"3__excel", CC_path+"\\"+"3__2Dtext")
        except FileExistsError:
            print("해당폴더명이 존재합니다.")
            shutil.rmtree(CC_path+"\\"+"1_subtitles")  # 폴더삭제
            shutil.rmtree(CC_path+"\\"+"3_2Dtext")  # 폴더삭제
            if "1__srt" in a:
                os.rename(CC_path+"\\"+"1__srt", CC_path+"\\"+"1__subtitles")
            elif "3__excel" in a:
                os.rename(CC_path+"\\"+"3__excel", CC_path+"\\"+"3__2Dtext")