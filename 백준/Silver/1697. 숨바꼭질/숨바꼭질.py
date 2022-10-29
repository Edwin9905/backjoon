from collections import deque
start, end = map(int,input().split())
q = deque()

dx = [1,-1,2]
visited = [0 for i in range(100001)]
q.append(start)

while q :
    start= q.popleft()
    if start == end :
        print(visited[start])
        exit()
    for i in range(3):
        if i == 2 :
            nx = dx[i] * start
        else :
            nx = dx[i] + start
        if 0<=nx<=100000 and not visited[nx]:
            visited[nx] = visited[start] + 1
            q.append(nx)
