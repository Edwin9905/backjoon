from collections import deque
lst = list()
for _ in range(int(input())) :
    lst.append(int(input()))
stk = []
i = 1
j = 0
ret = []
while i <= len(lst):
    stk.append(i)
    ret.append("+")
    while len(stk) and stk[-1] == lst[j] and j <= len(lst)-1:
        stk.pop()
        ret.append("-")
        j += 1
    i += 1
if len(stk) == 0:
    for i in ret:
        print(i)
else :
    print("NO")