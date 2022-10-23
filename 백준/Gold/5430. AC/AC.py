import sys
from collections import deque
input = sys.stdin.readline
for _ in range(int(input())):
    err = 0
    com = input()
    arrlen = int(input())
    arlen = arrlen
    #table = str.maketrans('[]','  ')
    #arr = deque(map(int,input().translate(table).split(',')))
    arr = deque(input().rstrip()[1:-1].split(","))
    i = 0
    cnt = 0
    while i < len(com)-1:
        if com[i] == 'R':
            cnt += 1
        elif com[i] == 'D':
            if arrlen == 0:
                print("error")
                err = 1
                break
            else :
                if cnt % 2 == 0 :
                    arr.popleft()
                else :
                    arr.pop()
            arrlen -= 1
        i +=1
    if not err :
        if cnt % 2 != 0 and arlen:
            arr.reverse()
        print('[',end='') 
        print(",".join(map(str,arr)),end=']\n')
        #print("[" + ",".join(arr) + "]")