length = int(input())

while length:
    time, str = map(str, input().split())
    int(time)
    i = 0
    while str[i]:
        print(str[i]*time)
    length -= 1