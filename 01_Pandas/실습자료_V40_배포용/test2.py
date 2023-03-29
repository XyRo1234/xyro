import sys

# def input_data():
#     map_soli = [[0] + list(readl().strip()) + [0] if 1<=r<=5 else [0]*11 for r in range(7)]
#     readl()
#     return map_soli

# readl = sys.stdin.readline
# T = int(readl())
# for _ in range(T):
#     # 입력받는 부분
#     map_soli = input_data()
#     # 여기서부터 작성
#     print(map_soli)


a = [1,2,3,4,5]
b = {'d1':'하하', 'd2':'호호'}
print(a.index(2))
b['d3'] = '크크'
print(b)


'''
3
###...###
..oo.....
.....oo..
.........
###...###

###...###
..oo.o...
...o.oo..
...oo....
###...###

###o..###
.o.oo....
o.o......
.o.o.....
###...###

'''