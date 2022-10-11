str = input()
ret = [0]*26
for i in range(0,len(str)) :
    tmp = ord(str[i]) - 97
    ret[tmp] += 1
for i in ret :
    print(i,end=" ")