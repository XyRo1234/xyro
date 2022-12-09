a_input = '4 5'

b_input = '''
00110
00011
11111
00000
'''

# 2차원 리스트의 맵 정보 입력 받기
n, m  = map(int, input().split())
gragh = []
for i in range(n):
    gragh.append(list(map(int,input())))

def dfs(x,y):
    if x<=-1 or x>=n or y<=-1 or y >=m:
        return False
    if gragh[x][y] == 0:
        gragh[x][y] = 1
        dfs(x-1,y)
        dfs(x,y-1)
        dfs(x+1,y)
        dfs(x,y+1)
        return True
    return False

result = 0
for i in range(n):
    for j in range(m):
        if dfs(i,j) == True:
            result += 1

print(result)


