import sys
from collections import deque
input = sys.stdin.readline
qlen, retlen = map(int,input().split())
ret = list(map(int,input().split()))
que = deque([i for i in range(1,qlen+1)])
i = 0
cnt = 0
while ret :
    while ret[i] == que[0] :
        if i == len(ret) -1 :
            print(cnt)
            exit()
        i += 1
        que.popleft()
    find = ret.index(ret[i])
    if que.index(ret[i]) <= (len(que)-1)//2:
        while ret[i] != que[0] :
            que.append(que.popleft())
            cnt += 1
    if que.index(ret[i]) > (len(que)-1)//2:
        while ret[i] != que[0] :
            que.appendleft(que.pop())
            cnt += 1
print(cnt)