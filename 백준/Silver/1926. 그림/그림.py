import sys
from collections import deque
input = sys.stdin.readline

def bfs(x, y) :
    max = 1
    global visited
    global borad
    queue = deque()
    queue.append([x,y])
    visited[x][y] = True

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < col and 0 <= ny < row:
                if borad[nx][ny] == 1 and not visited[nx][ny]:
                    visited[nx][ny] = True
                    queue.append([nx,ny])
                    max += 1
    return max

col, row = map(int,input().split())
visited = [[False]* row for _ in range(col)]
borad = [list(map(int,input().split())) for _ in range(col)]

dx = [-1,1,0,0]
dy = [0,0,-1,1]

cnt , max_val = 0,0
for i in range(col) :
    for j in range(row) :
        if borad[i][j] == 1 and not visited[i][j]:
            cnt += 1
            max_val = max(max_val,bfs(i,j))
print(cnt)
print(max_val)