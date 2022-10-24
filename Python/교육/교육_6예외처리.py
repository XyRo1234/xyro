## 예외처리
## 예외처리
nums = [1,2,3]

try:
    num1 = 6
    num2 = "삼"
    # print(num1/num2)
    # int("삼")
    print(int(6/0))
    # nums[3]
except TypeError:
    print("타입에러! 잘못된 값입니다.")
except ValueError:
    print("Value가 잘못되었습니다.")
except ZeroDivisionError as err:
    print(err)                      # 에러 문구 표시
except IndexError:
    print("인덱스에러")              # 이방법 혹은 아래방법 사용
except Exception as err:
    print("알수없는 에러가 발생하였습니다.")
    print(err)                      # 에러 문구 표시


## 에러 발생시키기
## 에러 발생시키기
try:
    print("한자리 숫자 나누기 전용 계산기입니다.")
    num1 = int(10)                      # 
    num2 = int(9)                       # 
    if num1 >= 10 or num2 >= 10:
        raise ValueError                                        # raise 사용하여 에러를 발생시킴.
    print("{0}/{1}={2}".format(num1, num2, int(num1/num2)))
except ValueError:
    print("잘못된 값을 입력하였습니다. 한자리 숫자만 입력하세요.")

## 사용자 정의 예외처리
## 사용자 정의 예외처리
class BigNumberError(Exception):        # 사용자가 정의한 예외처리
    pass

try:
    print("한자리 숫자 나누기 전용 계산기입니다.")
    num1 = int(10)                      # 
    num2 = int(9)                       # 
    if num1 >= 10 or num2 >= 10:
        raise BigNumberError                                    # raise 사용하여 에러를 발생시킴. // 사용자정의 BigNumberError 에러 사용
    print("{0}/{1}={2}".format(num1, num2, int(num1/num2)))
except BigNumberError:
    print("BigNumberError 발생")

## finally
## finally
try:
    print("한자리 숫자 나누기 전용 계산기입니다.")
    num1 = int(10)                      # 
    num2 = int(9)                       # 
    if num1 >= 10 or num2 >= 10:
        raise BigNumberError                                    # raise 사용하여 에러를 발생시킴. // 사용자정의 BigNumberError 에러 사용
    print("{0}/{1}={2}".format(num1, num2, int(num1/num2)))
except BigNumberError:
    print("BigNumberError 발생")
finally:
    print("에러발생 하든 안하든 실행됨")                        # finally는 에러발생 유무와 상관없이 실행됨
