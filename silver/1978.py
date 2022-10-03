ln = int(input())
nums = list(map(int,input().split(' ')))
ret = 0
for i in nums :
    j = 2
    while j < i :
        if i % j == 0 :
            break
        j += 1
    if i == j :
        ret += 1
print(ret)