import sys
input = sys.stdin.readline
cnt = 0
str = input().rstrip()
stack = []
tmp = 1
for i in range(len(str)) :
    if str[i] == '(':
        stack.append(str[i])
        tmp *= 2
    elif str[i] == '[':
        stack.append(str[i])
        tmp *= 3
    elif str[i] == ')':
        if not stack or stack[-1] == '[':
            cnt = 0
            break
        if str[i-1] == '(':
            cnt += tmp
        stack.pop()
        tmp //= 2
    else :
        if not stack or stack[-1] == '(':
            cnt = 0
            break
        if str[i-1] == '[':
            cnt += tmp
        stack.pop()
        tmp //= 3
if stack:
    print(0)
else:
    print(cnt)