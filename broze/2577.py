a = int(input())
b = int(input())
c = int(input())

ret = a * b * c
lit = []
while ret:
    lit.append(ret%10)
    ret //= 10

cnt = [0] * 10
for i in lit:
    cnt[i] += 1

for i  in cnt:
    print(i)