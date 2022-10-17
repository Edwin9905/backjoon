n = int(input())
nums = list(map(int,input().split()))
ret = []
stack = []
for i in range(n) :
    while stack:
        if nums[stack[-1]] >= nums[i] :
            break
        else :
            stack.pop()
    if stack:
        ret.append(stack[-1]+1)
    else :
        ret.append(0)
    stack.append(i)
print(*ret, sep = ' ')