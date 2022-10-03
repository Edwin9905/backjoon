n = int(input())
for i in range(n) :
    cnt = 0
    a = list(map(str, input()))
    for i in a :
        if i == '(' :
            cnt += 1
        elif i == ')' :
            cnt -= 1
        if cnt < 0 :
            break
    if cnt != 0 :
        print ("NO")
    else:
        print("YES")