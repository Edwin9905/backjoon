len = int(input())
answer = []
while len:
    a, b = map(int, input().split())
    answer.append(a+b)
    len -= 1
for an in answer:
    print(an)