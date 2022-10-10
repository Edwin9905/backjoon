a, b = map(int,input().split())
if a == b:
    print(0)
    exit()
if a > b :
    tmp = b
    b = a
    a = tmp
a += 1
print(b-a)
for i in range(a,b) :
    print(a, end= " ")
    a += 1