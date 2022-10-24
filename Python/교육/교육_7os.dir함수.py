import os
import glob
import shutil   # 파일옴기기

path = 'D:\\Program Files\\Workspace\\00_Default\\' # 경로1
path1 = 'D:\\Program Files\\Workspace\\00_Create\\' # 경로2

filename = "test.txt"

os.mkdir('folder')  # 폴더만들기
os.listdir()        # 모든파일,디렉토리명 리스트뽑기
os.rmdir('folder')  # 폴더삭제 (안에 파일이 없어야함)
os.remove("파일명") # 파일삭제
shutil.rmtree("폴더 or 파일명") # 폴더와 안의 파일 모두 지울수있습니다. 
os.rename(path+"\\"+"폴더명or파일명", path+"\\"+"폴더명2or파일명2")
shutil.move(path + filename, path1 + filename) # 파일옴기기
glob.glob('*.txt')  # 인자의 패턴과 이름이 일치하는 모든파일,디렉토리명 리스트뽑기

""" os.walk() """           
# 하위 폴더들까지 싹 뒤져서 파일들을 찾아줌. (path, dir, files) 에서 path는 str이고, dir과 files는 list형태이다.
# 하기처럼 사용하여, path + \\ + filename 을 만들 수 있다.
for (path, dir, files) in os.walk(path):
    for filename in files:
        print(path + "\\" + filename)
print("\n")

""" os.path.dirname(path) """
a = os.path.dirname(path)   # 경로를 반환한다. (파일명이 있으면 파일명은 제외되어 반환된다.)
print(a)

""" os.path.exists """
b = os.path.exists(path)    # 입력받은 path가 존재하면 True, 존재하지 않으면 False를 반환한다.
print(b)

# OS의 형식에 맞게 각가의 경로들을 하나의 경로로 이어준다. (복수경로도 이어줌 (a,b,c = a\b\c))
c = os.path.join(path, filename)
print(c)

""" os.path.split """
d = os.path.split('/Users/Desktop/temp/test.txt') # path를 디렉토리와 분리한다.
print(d)


""" 그외 기타 """
# path의 절대경로를 반환한다. (D:\Program Files\Workspace\test.txt)
os.path.abspath("test.txt")

# 경로의 기본이름을 반환한다. 파일명이나 폴더명 반환 (abspath와 반대되는 함수)  ('test.txt')
os.path.basename(r'D:\Program Files\Workspace\test.txt')

os.path.getsize('/Users/Desktop/temp/test.txt')  # path의 파일크기를 바이트단위로 반환한다. 

os.path.isdir('/Users/Desktop/temp/test.txt')    # path가 디렉토리이면 True, 아니면 False를 반환한다.


def createFolder(directory):
        try:
            if not os.path.exists(directory):
                os.makedirs(directory)
        except OSError:
            print ('Error: Creating directory. ' +  directory)





from_ = './mydir/myfile.txt'
to_ = './yourdir'

shutil.move(from_, to_)
