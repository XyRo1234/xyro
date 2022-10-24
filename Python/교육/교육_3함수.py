# def
# def
# 함수기본1
def open_def():                 # 함수정의, 함수명
    print("함수가 실행되었습니다")   # 함수를 외부에서 실행하면, 출력됨

open_def()      # 함수실행



# 함수기본2
def bankbook(balance, money):   # 함수명(인자1, 인자2) 해당인자는 함수내에서만 사용됨
    if balance >= money:
        print(f"출금 후 잔액은 {balance-money}원입니다.")
        return balance-money    # 함수실행 후 해당값 반환
    else:
        print(f"잔액이 부족합니다.잔액은 {balance}원입니다.")

balance = 50000
bankbook(balance,10000)  # 함수실행 (인자1=50000, 인자2=10000)



# 기본값
# 기본값
def profile(name, age=17 , main_lang='한국어'): # 함수를 불러올때 값이 없을시, 미리 지정해둔 값을 사용
    print(name, age , main_lang)

profile("철수")   # 함수실행 (name에 "철수" 입력됨)



# 키워드값
# 키워드값
def profile(name, age , main_lang):
    print(name, age , main_lang)

profile(main_lang='한국어', age=25, name='영희')    # 키워드값을 넣어서 작성하면 순서는 상관없음



# 가변인자
# 가변인자
    # *language
def profile(name, age , *language): # language가 수량이 일정치 않을때 * 를 사용하여 사용.
    print(name, age)
    for lang in language:
            print(lang, end=" ")    # (end=" ")는 다음줄로 넘어가지 않고, space한칸만 띄우고 옆에 다음 print를 하라는 의미

profile("철수", 20, "한국어", "영어", "일본어", "중국어", "불어", "스페인어")
print("")   # 마지막줄도 (end=" ")적용을 받고 있어서, 다음 함수실행시 적용되지 않도록 하기위해, 더미print를 한번 함.



# 지역변수, 전역변수
# 지역변수, 전역변수
    # global vest   # 전역변수 : 전역에서 사용되는 변수를 함수내에서 사용하겠다.
    #               # 지역변수 : 함수내에서만 사용하는 변수
vest = 10
def checkpoint(survivor):
    global vest      # 전역변수를 가져와서 사용하겠다.
    vest = vest - survivor
    print(vest)

checkpoint(4)   # 함수실행



# 표준입출력
# 표준입출력
print("Python", "Java", sep=" vs ", end=" ")    # sep : index값과 index값 사이에 삽입됨.
print("")                                       # end : 문장의 끝이 줄바꿈을 안하게 하고, " "사이의 단어를 출력.(줄바꿈은 사라짐)
scores = {"수학":0, "영어":50, "코딩":100}
for subject, score in scores.items():
    print(subject.ljust(8), str(score).rjust(4), sep=":")       # .ljust(8)  8칸을 확보하고, 그안에서 왼쪽정렬
                                                                # .rjust(4)  4칸을 확보하고, 그안에서 오른쪽정렬
a=1
print(str(a).zfill(3))                                          # .zfill(3)  3칸을 확보하고, 남은구간을 0 으로 채움.
# .ljust(8)     .rjust(4)   .zfill(3)
#   .   .   .   .   .   .   .


# 다양한 출력포맷
# 다양한 출력포맷
print("{0:_<+15,}".format(10000000))    # (_)빈자리"_"넣기, (<)왼쪽정렬, (+)+-부호붙이기, (15)자릿수확보, (,)3자리콤마넣기
print("{0:.2f}".format(5/3))            # 특정소수점자리수까지만 표시(현재2자리까지표시)

