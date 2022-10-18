import sys
from collections import deque
input = sys.stdin.readline
que = deque()
n = int(input())
for _ in range(n) :
    command = input().split()
    if command[0] == "push_front" :
        que.appendleft(command[1])
    if command[0] == "push_back" :
        que.append(command[1])
    if command[0] == "pop_front" :
        if que:
            print(que.popleft())
        else :
            print(-1)
    if command[0] == "pop_back" :
        if que:
            print(que.pop())
        else :
            print(-1)
    if command[0] == "size" :
        print(len(que))
    if command[0] == "empty" :
        if que:
            print(0)
        else :
            print(1)
    if command[0] == "front" :
        if que:
            print(que[0])
        else :
            print(-1)
    if command[0] == "back" :
        if que:
            print(que[-1])
        else :
            print(-1)