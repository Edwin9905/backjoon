import sys
from collections import deque
import copy
input = sys.stdin.readline

n = int(input())
graph = [list(map(str,input().rstrip())) for i in range(n)]
graph2 = copy.deepcopy(graph)
dx = [1,-1,0,0]
dy = [0,0,1,-1]
rgb1 = [0]*3
rgb2 = [0]*2

def bfs(b,x,y,color):
    q = deque()
    q.append((x,y))

    while q :
        x,y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<n and 0<=ny<n:
                if b[nx][ny] in color:
                    b[nx][ny] = 'D'
                    q.append((nx,ny))
            

for i in range(n):
    for j in range(n):
        if graph[i][j] == 'R':
            rgb1[0] += 1
            bfs(graph,i,j,'R')
        elif graph[i][j] == 'G':
            rgb1[1] += 1
            bfs(graph,i,j,'G')
        elif graph[i][j] == 'B':
            rgb1[2] += 1
            bfs(graph,i,j,'B')

for i in range(n):
    for j in range(n):
        if graph2[i][j] == 'R' or graph2[i][j] == 'G':
            rgb2[0] += 1
            bfs(graph2,i,j,'RG')
        elif graph2[i][j] == 'B':
            rgb2[1] += 1
            bfs(graph2,i,j,'B')

print(sum(rgb1),sum(rgb2))