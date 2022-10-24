# https://www.youtube.com/watch?v=dTDoTR0MXjU&t=577s
import re

#       [abc]       a나 b나 c가 들어있는 값 매치  = [a-c]
#       a.b         줄바꿈을 제외한 모든 문자와 매치 "a아무글이나있으면매치b"
#반복   ca*t        a가 몇번 반복되든 매치      "ct" "cat" "caat" ...
#반복   ca+t        a가 1번이상 반복되면 매치   "cat" "caat" ...
#반복   ca{2}t      a가 2번 반복되면 매치       "caat"
#반복   ca{2,4}     a가 2번이상 4번이하 반복되면 매치   "caat" "caaat" "caaaat"
#반복   ab?c        b가 0번,1번 반복되면 매치   "ac" "abc"


## compile, match
## Search, findall, finditer
p = re.compile('[a-z]+')    # 소문자 영어로 되어있는 문자열은 찾음
m = p.match('3python')       # 소문자로 이루어져있어서 매치됨
print(m)
m = p.match(' python')      # 숫자가 끼어있어서 매치안됨
print(m)
m = p.search('3 python')    # search는 숫자가 있어도 찾아줌
print(m)
m = p.findall('life is too short') # 일치하는 string를 리스트에 담아서 리턴해줌 ['life', 'is', 'too', 'short']
print(m)
m = p.finditer('life is too short') # iterator object가 리턴됨, 매치객체들이 담김 match('life'), match('is'), ...


# .group()  매치된 문자열을 리턴
# .start()  매치된 문자열의 시작위치 리턴
# .end()    매치된 문자열의 끝위치 리턴
# .span()   매치된 문자열의 (시작,끝)에 해당되는 튜플을 리턴
m = p.match('python')
print(m.group())    # python
print(m.start())    # 0
print(m.end())      # 6
print(m.span())     # (0,6)


# 컴파일 옵션
# 컴파일 옵션
# DOTALL, S         # 줄바꾸문자도 포함해서 compile하는 옵션
# IGNORECASE, I     # 소문자,대문자 구분없이 찾음
# MULTILINE, M      # 모든 줄 검사
# VERBOSE, X        # 엄청 긴 정규표현식을 나눠서(줄바꿈) 작성할수있도록 해줌
p = re.compile('a.b', re.S)     # DOTALL
print(p.match('a\nb'))          # DOTALL
p = re.compile('[a-z]+', re.I)  # IGNORECASE
print(p.match('Python'))        # IGNORECASE
print("Multiline")
p = re.compile('python', re.M)  # MULTILINE
data = """python one
life is too short
python two
you need python
python tree"""
print(p.findall(data))          # MULTILINE


## 메타문자
## 메타문자
# | : or
# ^ : 맨처음    ^Life
# $ : 맨끝      Life$
# \b : 공백     \bLife
# \s : 공백     \b랑 \s랑 뭐가다른거지????
# \w : 문자,숫자,_ 한개


# 그루핑 ()
p = re.compile('(ABC)+')    # ABC 반복
m = p.search('ABCABCABC')
print(m)
p = re.compile(r"(\w+)\s+\d+[-]\d+[-]\d+")
m = p.search("Park 010-1234-1234")
print(m)
print(m.group(1))           # 1번째 그룹을 리턴
# 그루핑된 문자열에 이름 붙이기 ?P<name>
p = re.compile(r"(?P<name>\w+)\s+\d+[-]\d+[-]\d+")
m = p.search("JUNG 010-1234-1234")
print(m.group("name"))      # name이라는 이름의 그룹을 리턴


# 전방탐색 : 긍정형 (?=)
p = re.compile(".+(?=:)")   # [.:문자] [+:반복] [():그루핑] [?=: : :가 검색조건에는 포함되나 리턴시에는 포함되지 않음]
m = p.search("http://google.com")
print(m.group())
# 전방탐색: 부정형 (?!)
p = re.compile(".*[.](?!bat$).*$", re.M)    # bat 제외?
m = p.findall("""
autoexec.exe
autoexec.bat
autoexec.jpg
""")
print(m)

# 문자열 바꾸기 sub

# Greedy vs Non-Greedy
    # <.*>사이의 문자열을 찾으면 전체를 지정해버림
    # <.*?>





# def extract_string(target):
#     return re.sub(r'<[^)]*>','',target)

# test = 'asdfa<aaa>'
# print(extract_string(test))