import sys
from collections import deque
input = sys.stdin.readline
t = int(input())

for _ in range(t) :
    flag = False
    m, n = map(int,input().split())
    graph = []
    q = deque()

    for i in range(n) :
        graph.append(list(input().rstrip()))
        for j in range(len(graph[i])) :
            if graph[i][j] == '*':
                q.append((-1, i, j))
            if graph[i][j] == '@':
                q.appendleft((0, i, j))

    dx = [0,0,1,-1]
    dy = [1,-1,0,0]

    while q:
        time,x,y = q.pop()

        if time > -1 and (x == 0 or y == 0 or x == n - 1 or y == m -1):
            flag = True
            print(time+1)
            break
        if time > -1 and graph[x+1][y] == '*' and graph[x-1][y] == '*' and graph[x][y+1] == '*' and graph[x][y-1] == '*' :
            break
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] != '#' :

                if time > -1 and graph[nx][ny] == '.':
                    graph[nx][ny] = '!'
                    q.appendleft((time+1,nx,ny))

                elif time == -1 and graph[nx][ny] != '*' and graph[nx][ny] != '!':
                    graph[nx][ny] = '*'
                    q.appendleft((-1,nx,ny))

    if not flag:
        print("IMPOSSIBLE")