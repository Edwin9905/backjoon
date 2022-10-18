from collections import deque
import sys
input = sys.stdin.readline
n = deque([i for i in range(1,int(input())+1)])
while len(n) != 1:
    n.popleft()
    n.append(n.popleft())
print(n[0])