
# if
# if
# if, elif, else , input
#weather = input("오늘 날씨는 어때요? ") # 유저가 입력하는 창이 뜸
weather = "미세먼지"
if weather == "비" or weather == "눈":
    print("우산을 챙기세요")
elif weather == "미세먼지":
    print("마스크챙기세요")
else:
    print("준비물 필요없어요")



# for
# for
for waiting_no in [1,2,3,4]:                # 
    print("대기번호 : %s" %waiting_no)


# while
# while
customer = "토르"
index = 5
while index >=1:
    print("%s님, 커피가 준비되었습니다. %s번 남았어요." % (customer,index) )
    index -= 1
    if index == 0:
        print("커피는 폐기처분되었습니다.")

#while True:
#    print("%s님, 커피가 준비되었습니다. 호출 %s회" %customer)   #무한루프 탈출은 ctrl+C


# continue
# continue
absent = [2,5]  # 결석
no_book = [6]   # 책을 깜빡했음. 리스트로 표현해야하네
for student in range(1,7):
    if student in absent:
        continue                        # 처음으로 돌아가서 다음 index진행
    elif student in no_book:
        print("오늘수업여기까지. %s는 교무실로 따라와" %student)
        break                           # 반복문을 아예 끝내버림
    print("%s번, 책을 읽어봐" %student)


# 한줄 for
# 한줄 for
# 출석번호가 1,2,3,4... 앞에 100을 붙이기로함. 101,102,103,...
students = [1,2,3,4,5]
print(students)
students = [i+100 for i in students]
print(students)

students = ["Iron man", "Thor", "I am groot"]
students = [len(i) for i in students]
print(students)





"""
업로드용
"""

# if
# if, elif, else , input
condition = "normal"

if condition == "bad" or condition == "worst":
    print("컨디션이 안좋아요")
elif condition == "normal":
    print("그냥그래요")
else:
    print("컨디션 좋아요")


# for
for a in [1,2,3,4]: 
    print(a)


# while
index = 4
while index >=1:
    print("현재숫자는 %s입니다." % (index))
    index -= 1
    if index == 0:
        print("현재숫자 0으로 종료합니다.")
