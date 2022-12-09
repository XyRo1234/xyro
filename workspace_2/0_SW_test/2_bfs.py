from collections import deque

'5 6'

'''
101010
111111
000001
111111
111111
'''

n, m = map(int, input().split())
gragh = []
for i in range(n):
    gragh.append(list(map(int,input())))

dx = [1,0,-1,0]
dy = [0,1,0,-1]

def bfs(x,y):
    queue = deque()
    queue.append((x,y))
    # 큐가 빌 때까지 반복하기
    while queue:
        x,y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 미로찾기 공간을 벗어난 경우 무시
            if nx < 0 or nx >=n or ny <0 or ny >=m:
                continue
            # 벽인 경우 무시
            if gragh[nx][ny] == 0:
                continue
            if gragh[nx][ny] == 1:
                gragh[nx][ny] = gragh[x][y] + 1
                queue.append((nx,ny))
    # 가장 오른쪽 아래까지의 최단거리 반환
    return gragh[n-1][m-1]

print(gragh)
print(bfs(0,0))
