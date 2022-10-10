lst = []
sum = 0
for _ in range(5) :
    lst.append(int(input()))
lst.sort()
for i in lst :
    sum += i
print(sum//5)
print(lst[2])