
import sys
from collections import deque
   
def Input_Data():
    readl = sys.stdin.readline
    M, N = map(int,readl().split())
    K = int(readl())
    list_bus = [list(map(int,readl().split())) for _ in range(K)]
    sx, sy, dx, dy = map(int,readl().split())
    return M, N, K, list_bus, sx, sy, dx, dy
   
def Arange_Bus(list_bus):
    list_bus = [(id,min(x1,x2),max(x1,x2),min(y1,y2),max(y1,y2)) for id,x1,y1,x2,y2 in list_bus]
    return list_bus
   
def Make_Init():
    q = deque()
    s_rem = set(range(K))
    s_dest = [False]*K
    for i, bus in enumerate(list_bus):
        flag = 0
        _, x1, x2, y1, y2 = bus
        if x1<=dx<=x2 and y1<=dy<=y2:   # 목적지 넘버에 체크
            print(f'{x1,dx,x2} {y1,dy,y2}')
            s_dest[i]=True
        if not x1<=sx<=x2: continue
        if not y1<=sy<=y2: continue
        if s_dest[i]: return True, s_rem, s_dest, q # 목적지체크된곳에 시작지도 잇으면 리턴
        s_rem.remove(i) # 시작지 제외 목록
        q.append((i, 1)) # 
    return False, s_rem, s_dest, q
   
def Check(n,nn):
    return ((list_bus[n][1]<=list_bus[nn][1]<=list_bus[n][2]) or (list_bus[nn][1]<=list_bus[n][1]<=list_bus[nn][2])) and ((list_bus[n][3]<=list_bus[nn][3]<=list_bus[n][4]) or (list_bus[nn][3]<=list_bus[n][3]<=list_bus[nn][4]))

# [(1, 2, 2, 1, 2), (2, 1, 5, 1, 1), (6, 7, 7, 3, 6), (7, 2, 2, 1, 6), (3, 3, 6, 2, 2), (4, 5, 5, 1, 6), (5, 1, 7, 5, 5), (8, 3, 6, 5, 5)]
def BFS():
    arrived, s_rem, s_dest, q = Make_Init()
    if arrived: return 1
    while q:
        n, cnt_bus = q.popleft()    # 버스넘버(-1) / 버스카운트 1
        s_chk = list()
        ncnt_bus = cnt_bus + 1
        for nn in s_rem:
            if not Check(n, nn): continue
            if s_dest[nn]: return ncnt_bus  # nn버스에 목적지가 있으면 리턴
            s_chk.append(nn)        # s_chk에 nn버스 추가
            q.append((nn, ncnt_bus))    # (버스넘버, 갈아타기횟수+1)
            print(f'n:{n}번버스와 겹치는 버스, s_chk(인덱스):{s_chk}, {q}')
        for i in s_chk:
            s_rem.remove(i)
        print(f's_rem:{s_rem}, s_chk:{s_chk}, {q}')
        print('')
    return -1
   
ans = -1 
# 입력 받는 부분
M, N, K, list_bus, sx, sy, dx, dy = Input_Data()
 
# 여기서부터 작성
list_bus = Arange_Bus(list_bus)
list_bus.sort()
print(list_bus)
ans = BFS()
 
# 출력하는 부분
print(ans)

'''

7 6
8
1 2 1 2 2
2 1 1 5 1
6 7 3 7 6
7 2 1 2 6
3 3 2 6 2
4 5 6 5 1
5 1 5 7 5
8 3 5 6 5
2 1 7 4

'''