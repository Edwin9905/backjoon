n , m = map(int,(input().split()))
lst = list(map(int,input().split()))
ret = 0
for i in range(0,len(lst)) :
    for j in range(i+1,len(lst)) :
        for z in range(j+1,len(lst)) :
            tmp = lst[i] + lst[j] + lst[z]
            if ret < tmp <= m :
                ret = tmp
print(ret)