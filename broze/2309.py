a = []
for i in range(9):
    a.append(int(input()))
for i in range(9):
    j = i+1
    while j <= len(a) -1:
        if (sum(a) - (a[i] + a[j]) == 100):
            del a[i]
            del a[j-1]
            a.sort()
            for i in a:
                print (i)
            exit()
        j += 1