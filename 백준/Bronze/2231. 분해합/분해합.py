n = int(input())
i = 0
while i != n:
    lst = []
    tmp = i
    l = len(str(tmp))
    times = 1
    for _ in range(l-1) :
        times *= 10
    for _ in range(l) :
        lst.append((tmp//times)%10)
        times //= 10
    if i + sum(lst) == n :
        print(i)
        exit()
    i += 1
print(0)