import sys
input = sys.stdin.readline

n = int(input())
lst = list(map(int,input().split()))
lst.sort()
goal = int(input())
cnt = 0
left, right = 0, n - 1

while left != right :
    if lst[left] + lst[right] == goal:
        cnt += 1
        left += 1
    elif lst[left] + lst[right] > goal :
        right -= 1
    else :
        left += 1

print(cnt)