length = int(input())

while length:
    time, stra = map(str, input().split())
    time = int(time)
    i = 0
    while i < len(stra):
        print(stra[i]*time, end='')
        i += 1
    length -= 1
    print()