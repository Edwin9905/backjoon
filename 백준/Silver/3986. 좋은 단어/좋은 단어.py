import sys
input = sys.stdin.readline
cnt = 0
for _ in range(int(input())) :
    str = input().rstrip()
    i = 0
    stack = []
    for i in range(len(str)):
        if stack and stack[-1] == str[i] :
            stack.pop()
        else :
            stack.append(str[i])
    if not stack :
        cnt += 1
print(cnt)