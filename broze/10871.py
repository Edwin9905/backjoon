loop, std = map(int,input().split())
temp = input().split(' ')
i = 0
while loop:
    if int(temp[i]) < std:
        print(temp[i], end= " ")
    loop -= 1
    i += 1