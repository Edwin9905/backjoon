import sys
input = sys.stdin.readline
que = []
ret = []
for _ in (range(int(input()))) :
    command = list(map(str,input().strip().split()))
    if command[0] == "push" :
        que.append(command[1])
    if command[0] == "pop" :
        if que:
            ret.append(que.pop(0))
        else :
            ret.append(-1)
    if command[0] == "size" :
        ret.append(len(que))
    if command[0] == "empty" :
        if que:
            ret.append(0)
        else :
            ret.append(1)
    if command[0] == "front" :
        if que:
            ret.append(que[0])
        else :
            ret.append(-1)
    if command[0] == "back" :
        if que:
            ret.append(que[-1])
        else :
            ret.append(-1)
for i in ret:
    print(i)