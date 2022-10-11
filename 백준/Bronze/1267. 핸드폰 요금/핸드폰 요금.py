import math
n = int(input())
time = list(map(int, input().split()))
y = []
m = []
for i in time :
    y.append(i//30*10+10)
    m.append(i//60*15+15)
if sum(y) == sum(m) :
    print(f"Y M {sum(y)}",end= "")
else :
    if sum(y) > sum(m) :
        print (f"M {sum(m)}",end = "")
    else :
        print (f"Y {sum(y)}",end = "")