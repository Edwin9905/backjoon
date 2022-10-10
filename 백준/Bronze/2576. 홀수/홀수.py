import sys
lst = []
sum = 0
max = 999999
for _ in range(7) :
    tmp = int(sys.stdin.readline())
    lst.append(tmp)
    if tmp % 2 != 0:
        sum += tmp
        if max > tmp :
            max = tmp
if sum == 0 :
    print (-1)
else :
    print(sum)
    print(max)