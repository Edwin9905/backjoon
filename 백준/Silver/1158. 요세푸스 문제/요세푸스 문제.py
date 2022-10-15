n, k = map(int,(input().split()))
lst = [i for i in range(1,n+1)]
ret = []
loc = k-1
while len(lst):
    if loc >= len(lst) :
        loc -= len(lst) * (loc // len(lst))
    ret.append(lst[loc])
    lst.pop(loc)
    loc -= 1
    loc += k

print("<",end="")
for i in range(0,len(ret)) :
    if i == len(ret)-1:
        print(ret[i],end="")
        print(">")
    else :
        print(f"{ret[i]}, ",end="")