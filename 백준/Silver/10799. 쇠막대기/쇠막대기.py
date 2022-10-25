import sys
input = sys.stdin.readline
cnt = 0
str = input().rstrip()
stack = []
for i in range(len(str)) :
    if str[i] == '(':
        stack.append(str[i])
    else :
        if str[i-1] == '(':
            stack.pop()
            cnt += len(stack)
        else : 
            stack.pop()
            cnt += 1
print(cnt)