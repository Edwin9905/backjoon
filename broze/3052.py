lst = []
for _ in range(10):
    lst.append(int(input()))
ret = set([i % 42 for i in lst])
print(len(ret))