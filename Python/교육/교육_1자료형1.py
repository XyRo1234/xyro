# 전체주석 : ctrl + K + C
# 전체주석취소 : ctrl + K + U

#자료형
# 문자형 str / 정수형 int / 실수형은 float
d = "냉장고"
a=3
b=4
str(d)  # 문자형으로 변환
int(a)      # 정수형으로 변환
float(b)    # 실수형으로 변환

print(a+b)
print(a/b)  #나누기 값
print(a//b) #나누기 몫
print(a%b)  #나누기 나머지
print(d**2) # 제곱


#문자열
#문자열 기본
# 참고로 순서는 1부터가 아닌 0부터 시작이다. [0,1,2,3,4,5,...]
e = "Life_is_good!"
print(e[0])     #e의 0번째(첫번째) 문자(결과: L)
print(e[-1])    # -1번째문자 (맨뒤문자)(결과: !)
print(e[:8])    #[이상:미만:간격] / [0이상8미만의 문자] (결과: Life_is_)
print(e[::-1])  #거꾸로 읽기 (결과: !doog_si_efiL)


#   문자열 포맷 코드
#   %s 문자열 / %c 문자1개 / %d 정수 / %f 부동소수
number = 10
day = "three"
a = "I_eat_%d_apples. I_was_sick_for_%s days" %(number,day)
b = "I_eat_%d_apples. I_was_sick_for_%s days" %(4,"two")
c = "%0.7f" %3.42134234 #소수점 7번째 자리까지만 표시한다
print(a)                # I_eat_10_apples. I_was_sick_for_three days
print(b)                # I_eat_4_apples. I_was_sick_for_two days
print(c)                # 3.4213423


#문자열
#문자열 기본2
a = "inhobby"
print(a.count('b'))             # 문자열 개수 세기 (count)
#문자 찾기
print(a.find('b'))              # index넘버(순서)를 출력함. (find)  # 'b'가 들어가있는 index값 4를 출력
print(a.find('x'))              # index넘버(순서)를 출력함. (find)  # 'x'는 없어서 -1을 출력함
print(a.join('abcd'))    #문자열 삽입 (a삽입b삽입c삽입d)            # ainhobbybinhobbycinhobbyd
print(a.upper())                # 소문자를 대문자로 바꾸기 (upper) / 대문자를 소문자로 바꾸기 (lower)
a = " hi jhon   "
print(a.strip())                #양쪽 공백 지우기(strip)           # 양쪽 공백만 지움 (결과: "hi jhon")
a = "Life is good"
print(a.replace("Life","LG"))   #문자열 교체하기 (replace)
print(a.split())                #문자열 나누기 (split)             # ['Life', 'is', 'good']


#리스트
#리스트기본
a = ["냉장고","세탁기","스타일러"]
print(a[1])     # index 1의 값 print                       / 결과: 세탁기
#리스트수정
a[0:2] = ["아이폰","갤럭시"]    # 0부터2미만 index에 값 삽입 / 결과: ['아이폰', '갤럭시', '스타일러']
print(a)
a[0:2] = []     # 0부터2미만의 index값에 NA를 삽입 (삭제)
print(a)        #                                         / 결과: ['스타일러']

a = [4,2,3]
a.append("청소기") #"청소기"를 리스트에 추가(append)       / 결과: [4,2,3,'청소기']
print(a)

a = ['Refrigerator','Washingmachine','Styler']
a.sort()        # 가나다 혹은 알파벳 순서대로 정렬(sort)   / 결과: ['Refrigerator', 'Styler', 'Washingmachine']
print(a)

a = [1,5,3]
a.insert(0,4)   # 0번째 index에 4값을 추가해라(삽입) (insert)  / 결과: [4, 1, 5, 3]
print(a)
a.remove(1)             # 1값을 삭제해라 (삭제) (remove)       / 결과: [4, 5, 3]
print(a)

a = [1,2,3]
print(a.pop())         # 리스트 요소 끄집어내기 (pop)         # print를 하면 끄집어내어진 값이 보임 (프린트: 3)
print(a)               # 맨 뒤에서부터 꺼냄                   # 마지막 3값이 사라짐... / 결과: [1, 2]

a = [1,2,3,1,1,1]
print(a.count(1))       #카운트(count)                       # 1값이 몇개인지 카운트 / 결과: 4

a = [1,2,3]
a.extend([4,5])         #확장(extend)                        # 4,5값 추가 / 결과: [1, 2, 3, 4, 5]
print(a)

a.reverse()             # 리스트 순서 뒤집기 (reverse)        # [5, 4, 3, 2, 1]


# 리스트 응용
# shuffle, sample, range&list
lst = [1,2,3,4,5]
from random import *    # random 함수 사용
shuffle(lst)           # shuffle : 리스트안의 values 순서를 랜덤으로 썪음
print(lst)
print(sample(lst,2))    # sample : sampling. 리스트에서 2개를 무작위로 뽑음
users = range(1,21)     # 1~21까지 리스트로 생성 [1,2,3, ... ,20, 21]
winners = sample(users,4)   # users리스트에서 4개 무작위 샘플링
print(winners)
print("치킨당첨자: {0}".format(winners[0]))     # index 0번
print("커피당첨자: {0}".format(winners[1:]))    # index 1,2,3번


#튜플
t1 = (1,2,'a','b')              # 리스트는 [대괄호] / 튜플은 (소괄호)  # 튜플은 수정이할 수 없다.

#사전 (dictionary)
dic = {'name':'Eric', 'age':15, 1:'a'}  # (dictionary)사전 / {Key:Value}
list(dic.keys())[0]                     # name
print(dic['name'])                      # Eric
print(dic[1])                           # a
dic['phone'] = "010-777-8888"           # dic에 추가됨
print(dic)                              # {'name': 'Eric', 'age': 15, 1: 'a', 'phone': '010-777-8888'}
del dic[1]                    # Key이름으로 지우기
print(dic)                    # {'name': 'Eric', 'age': 15, 'phone': '010-777-8888'}
print(dic.keys())           # key값만 얻기/      dict_keys(['name', 'age', 'phone'])
print(dic.values())         # value값만 얻기/    dict_values(['Eric', 15, '010-777-8888'])
print(dic.items())          # key, value값 얻기/ dict_items([('name', 'Eric'), ('age', 15), ('phone', '010-777-8888')])
# dic['adress']             # adress값 확인하기. adress가 없으면, Error발생하고 program 종료
print(dic.get('adress'))          # key값이 없을경우, None을 출력/ None
print(dic.get('adress','없음'))   # key값이 없을경우, 없음으로 내보내기/ 없음
print(4 in dic)             # 4 라는 key가 있냐? 없어서 False로 답함/ False
dic.clear()                 # 전체 삭제


# 자료구조의 변경
# 자료구조의 변경
menu = {"커피", "우유", "주스"}
print(type(menu))         # menu의 타입 확인 <class 'set'>
menu = list(menu)           # 타입이 list로 바뀜 <class 'list'>
menu = tuple(menu)          # 타입이 튜플로 바뀜 <class 'tuple'>
menu = set(menu)            # 타입이 set로 바뀜 <class 'set'>


# 집합형
s1 = set([1,2,3])   # 집합형은 중복이 없고, 순서가 없다.
s1 = {1,2,3}        # {} 해당괄호로도 만들 수 있다.
a = ("hello")
print(a)            # hello
a = set("hello")    # 집합형은 중복이 없고, 순서가 없다.
print(a)            # 예시 {'l', 'h', 'e', 'o'}
s1 = set([1,2,3,4,5,6])
s2 = set([4,5,6,7,8,9])
print(s1 & s2)              # 교집합
print(s1.intersection(s2))  # 교집합(위와 같음)
print(s1 | s2)              # 합집합
print(s1.union(s2))         # 합집홥(위와 같음)
print(s1 - s2)              # 차집합
print(s1.difference(s2))    # 차집합(위와 같음)
s1.add(7)                   # 집합 값 추가하기
print(s1)
s1.update([7,8,9])          # 값 여러개 추가하기
print(s1)
s1.remove(9)                # 값 삭제하기
print(s1)

# 불 (참, 거짓)(boolean)
a=True              # "True" 참. T를 대문자로 써야함 // "False" 거짓. F를 대문자로 써야함
if a:                # a가 참이면, 실행. (참: 문자, 1) // (거짓: NA, 0, 괄호)
    print(a)
a = [1,2,3,4]
while a:            # [1, 2, 3, 4]참, [2, 3, 4]참, [3, 4]참, [4]참, []거짓
    print(a)
    del(a[0])
a = [1,2,3,4]
while a:            # [1, 2, 3, 4]참, [1, 2, 3]참, [1, 2]참, [1]참, []거짓
    print(a)
    a.pop()


# 숫자처리함수
# 숫자처리함수
print(abs(-5))      # 절대값함수 / 음수를 넣으면 양수가 나오고, 양수를 넣으면 양수가 나옴 (결과: 5)
print(pow(4,3))     # 제곱근 4^3 = 4x4x4 = 64
print(max(5,12))    # 최대값(결과: 12)
print(min(5,12))    # 최소값(결과: 5)
print(round(3.14))  # 3  - 반올림
print(round(4.99))  # 5  - 반올림

from math import *  # math 에서 *을 가져오기 (math 함수 사용)
print(floor(4.99))  # 내림          : 4
print(ceil(3.14))   # 올림          : 4
print(sqrt(16))     # 제곱근 16=2^4 : 4

from random import *    # random 함수 사용
random()     # 0.0~1.0 미만의 임의의 값 생성
random()*10  # 0.0~10.0 미만의 임의의 값 생성
int(random()*10) # int 정수
print(randrange(1,46)) # 1~46미만
print(randint(1,45))   # 1~45이하



# 문자열처리 함수
# 문자열처리 함수
# lower, upper, isupper, len, replace, index, find, count
python = "Python is Amazing"
python.lower()          # 전체소문자
python.upper()          # 전체대문자
python[0].isupper()     # index 0 이 대문자인지? : True
len(python)             # index 수량, 길이
a = python.replace("Python", "Java")    # (replace) Python을 Java로 변환
print(a)
index = python.index("n")               # (index) n이 들어있는 index위치 (5)
print(index)
index = python.index("n", index + 1)    # 2번째 n이 들어있는 index위치 (15)
print(index)
python.find("n")        # (find) index랑 똑같이 찾아줌. find는 없는걸 찾을때 -1을 반환함
python.count("n")       # (count) 는 n이 몇번 등장하는지 세어줌



# 문자열 포맷
# 문자열 포맷
# %d, %s, $c, {}.format
age = 20
color = "빨간색"
python = "Python is Amazing"
print("나는 %d살입니다." % age)     # %d 정수
print("나는 %s을 좋아해요." % python)   # %s 정수,문자
print("Apple은 %c로 시작해요" % "A")    # %c 한글자
print("나는 %s과 %s을 좋아해요" % ("파란색","녹색"))    # 2번이상입력
print("나는 {}살입니다.".format(20))    # (format)
print("나는 {}과 {}을 좋아해요".format("파란색","빨간색"))  # 2번이상입력
print("나는 {1}과 {0}을 좋아해요".format("파란색","빨간색"))# 순서지정도 가능
print("나는 {age}살이며 {color}을 좋아해요".format(age=21, color="돈"))
print(f"나는 {age}살이며 {color}을 좋아해요")   # 지정한 변수를 사용하려면 f 를 사용

# 하기 .format(age, color)의 경우, 파이썬 버전에 따라 실행이 안되기도 하는것 같습니다.
# age = "21"
# color = "빨간색"
# print("나는 {age}살이며 {color}을 좋아해요".format(age, color))



# 탈출문자
# [""]나 [\]의 경우, 문법적으로 쓰이는 경우가 많아서, 문장처럼 사용하려면 하기처럼 \를 앞에 붙여줘야한다.
print("나는 \"파이썬\"입니다.")     # 나는 "파이썬"입니다.
print("\\")                       # \
print("\n")                       # \n : 줄바꿈
# \r : 커서를 맨 앞으로 이동 및 덮어씌움   ex) "Red Apple\rPine"
print("0123Apple\rPine")          # 결과: PineApple
# \b : 백스페이스(한글자 삭제)      ex) "Redd\d Apple" = Red Apple
# \t : 탭                         ex) "Red\tApple"  = Red   Apple


# 리스트 []
# 리스트 []
# index, append, insert, pop, sort, reverse, clear, extend
subway = ["유재석", "김누구", "조세호"]
subway.index("조세호")
subway.append("박명수") # 맨뒤에 추가
subway.insert(1,"하하") # index를 지정해야함
subway.pop()            # 맨 뒤에서부터 꺼냄
subway.count("유재석")  # 유재석이 몇개(명)인지 숫자샘
subway.sort()           # 정렬
subway.reverse()        #리스트 순서 뒤집기
print(subway)
# subway.clear()          # 리스트 모두 지우기
list2 = [1,5,3]
subway.extend(list2)     # 리스트 확장(합치기)




# 사전 {}
# 사전 {}
#[], get, del, keys, values, items, clear
cabinet = {3:"유재석", 100:"김태호"}    # 3, 100 대신 문자도 가능
cabinet[3]                      # 만약, 3이 없다면, Error발생하고 program 종료
cabinet.get(3)                  # 만약, 3이 없어도, None을 출력하고 program 진행
cabinet.get(5, "사용가능")      # 5는 없기에, 5에 "사용가능"을 입력하고 출력
3 in cabinet        # 3이 있으므로, True / 만약,없으면, False 출력
cabinet[3] = "김종국"   # 추가, 또는 덮어쓰기

print(cabinet)
del cabinet[3]
cabinet.keys()          # keys들만 출력
cabinet.values()        # values들만 출력
cabinet.items()         # keys, valuse 출력
cabinet.clear()         # 전체 삭제


# 튜플 tuple ()
# 튜플 tuple ()
menu = ("돈까스", "치즈까스")


# 집합 (set) {}사용
# 집합 (set) {}사용
# {}, & intersection, | union, - difference, add, remove
set1 = {1,2,3,3,3}                   # {}로 묶고, 중복 안됨, 순서 없음
print(set1)
java = {"유재석","김태호","양세형"}
python = {"유재석","박명수"}
print(java & python)                # 교집합
print(java.intersection(python))    # 교집합
print(java | python)                #  합집합
print(java.union(python))           #  합집합
print(java - python)                # 차집합
print(java.difference(python))      # 차집합
python.add("김태호")    # set에 추가
java.remove("김태호")   # set에서 제거


# 자료구조의 변경
# 자료구조의 변경
menu = {"커피", "우유", "주스"}
print(type(menu))         # menu의 타입 확인 <class 'set'>
menu = list(menu)           # 타입이 list로 바뀜 <class 'list'>
menu = tuple(menu)          # 타입이 튜플로 바뀜 <class 'tuple'>
menu = set(menu)            # 타입이 set로 바뀜 <class 'set'>
