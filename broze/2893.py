input = int(input())
ret = 0
while input >= 0:
    if input % 5 == 0:
        ret += input//5
        print(ret)
        break
    input -= 3
    ret += 1
else :
    print(-1)