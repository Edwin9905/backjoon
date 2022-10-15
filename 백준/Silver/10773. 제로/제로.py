from collections import deque
stk = deque()
for _ in range(int(input())):
    command = int(input())
    if command == 0 and stk:
        stk.pop()
    else :
        stk.append(command)
print(sum(stk))