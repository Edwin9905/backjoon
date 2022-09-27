answer = []
flag = True
while flag:
    a, b = map(int, input().split())
    if a == b == 0:
        break
    answer.append(a+b)
for an in answer:
    print(an)