card = [i for i in range(1,21)]
for _ in range(10) :
    a, b = map(int,input().split())
    tmp = card[a-1:b]
    j = len(tmp) -1
    for i in range(a-1,b) :
        card[i] = tmp[j]
        j -= 1
for i in card :
    print(i, end=" ")