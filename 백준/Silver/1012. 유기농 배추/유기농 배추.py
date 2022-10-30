import sys
from collections import deque

input = sys.stdin.readline
dx = [1,-1,0,0]
dy = [0,0,1,-1]
def bfs(x,y) :
    global graph
    q = deque()
    q.append((x,y))

    while q :
        x,y = q.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0<=nx<row and 0<=ny<col and graph[nx][ny] == 1:
                graph[nx][ny] = 0
                q.append((nx,ny))

for _ in range(int(input())):
    row, col, n = map(int,input().split())
    graph = [[0] * col for i in range(row)]
    cnt = 0
    for _ in range(n):
        x, y = map(int,input().split())
        graph[x][y] = 1

    for i in range(row) :
        for j in range(col) :
            if graph[i][j] == 1:
                graph[i][j] = 0
                bfs(i,j)
                cnt +=1 
    print(cnt)
