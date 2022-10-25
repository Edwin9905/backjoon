import sys
from collections import deque
input = sys.stdin.readline

def bfs(x,y):
    val = 1
    q = deque()
    q.append([x,y])

    while q:
        x,y = q.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 1:
                val += 1
                q.append([nx,ny])
                graph[nx][ny] = 0
    return val

n, m = map(int,input().split())
graph = [list(map(int,input().split())) for i in range(n)]
cnt , max_val = 0, 0
dx = [1,-1,0,0]
dy = [0,0,1,-1]

for i in range(n) :
    for j in range(m) :
        if graph[i][j] == 1:
            graph[i][j] = 0
            cnt += 1
            max_val = max(max_val,bfs(i,j))

print(cnt)
print(max_val)