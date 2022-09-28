def cal(a):
    cnt = 0
    sum = 0
    for i in range(len(a)):
        if a[i] == 'O':
            cnt += 1
            sum += cnt
        else :
            cnt = 0
    return sum

length = int(input())
val = []
for i in range(length):
    val.append(cal(input()))
    length -= 1
for i in val:
    print(i)