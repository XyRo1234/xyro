# """클래스"""
# """클래스"""

name = "마린"
hp = 40
damage = 5

print("{0}유닛이 생성되었습니다.".format(name))
print("체력 {0}, 공격력 {1}\n".format(hp, damage))


## 일반유닛
## 일반유닛
class Unit:                                                         # 클래스 생성
    def __init__(self, name, hp, damage):                           # __init__ : 생성자
        self.name = name                                            # 여기서 생성된 name, hp, damage를 "맴버변수" 라고 한다.
        self.hp = hp
        self.damage = damage
        print("{0}유닛이 생성 되었습니다.".format(self.name))
        print("체력 {0}, 공격력 {1}".format(self.hp, self.damage))

marine1 = Unit("마린", 40, 5)   # 마린, 탱크를 "객체"라고 부르며,  Unit클래스의 "인스턴스" 라고 표현한다.
marine2 = Unit("마린", 40, 5)
tank = Unit("탱크", 150, 35)

wraith1 = Unit("레이스", 80, 5)
print("유닛 이름 : {0}, 공격력 : {1}".format(wraith1.name, wraith1.damage)) # 맴버변수를 가져와서 사용.

wraith2 = Unit("레이스", 80, 5)
wraith2.clocking = True             # class 외부에서 변수를 줄수있음. 단 wraith2 라고 지정한것처럼 특정변수에 지정함.

if wraith2.clocking == True:
    print("{0}는 현재 클로킹 상태입니다.".format(wraith2.name))


# 공격 유닛
# 공격 유닛
class AttackUnit:
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage
        print("{0} 유닛이 생성 되었습니다.".format(self.name))
        print("체력 {0}, 공격력 {1}".format(self.hp, self.damage))
    
    def attack(self, location):
        print("{0} : {1} 방향으로 적군을 공격 합니다. 공격력 : {2}".format(self.name, location, self.damage))

    def damaged(self, damage):
        print("{0} : {1} 데미지를 입었습니다.".format(self.name, damage))
        self.hp -= damage
        print("{0} : 현재 체력은 {1} 입니다.".format(self.name, self.hp))
        if self.hp <= 0:
            print("{0} : 파괴되었습니다.".format(self.name))

# 파이어뱃 : 공격유닛, 화염방사기.
firebat1 = AttackUnit("파이어뱃", 50, 16)
firebat1.attack("5시")
# 공격 2번 받는다고 가정
firebat1.damaged(25)
firebat1.damaged(25)

## 상속
## 상속

## 다중상속
## 다중상속

## 오버라이딩
## 오버라이딩

## pass
## pass

## super
## super
