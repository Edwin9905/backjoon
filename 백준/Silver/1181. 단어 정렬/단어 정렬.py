import sys
input = sys.stdin.readline

lst = []
for _ in range(int(input())) :
    lst.append(input().rstrip())
lst = list(set(lst))
lst.sort()
lst.sort(key = len)

for i in lst:
    print(i)