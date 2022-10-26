import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int,input().split())
graph = [list(map(int,input().split())) for i in range(m)]

dx = [0,0,1,-1]
dy = [1,-1,0,0]

def bfs(lst) :
    day = 0
    q = deque()
    flag = False
    while lst :
        tx,ty = lst.pop()
        for i in range(4):
            nx = dx[i] + tx
            ny = dy[i] + ty
            if 0 <= nx < m and 0 <= ny < n and graph[nx][ny] == 0:
                graph[nx][ny] = 1
                q.append([nx,ny])
    
    while q:
        nq = deque()
        while q:
            x,y = q.popleft()
            for i in range(4):
                nx = dx[i] + x
                ny = dy[i] + y
                if 0 <= nx < m and 0 <= ny < n and graph[nx][ny] == 0:
                    graph[nx][ny] = 1
                    nq.append([nx,ny])

        for i in range(len(nq)) :
            q.append(nq[i])
        nq.clear()
        day += 1

    for i in range(m) :
        for j in range(n) :
            if graph[i][j] == 0:
                flag = True
    if flag :
        return -1
    return day

ret = 0
start = []
for i in range(m) :
    for j in range(n) :
        if graph[i][j] == 1:
            start.append([i,j])
print(bfs(start))