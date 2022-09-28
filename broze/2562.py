val = []
len = 9
while len:
    val.append(int(input()))
    len -= 1
print(max(val))
print(val.index(max(val))+1)