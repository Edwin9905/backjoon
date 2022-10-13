import sys
input = sys.stdin.readline
for _ in range(int(input())) :
    command = list(input().rstrip())
    s1 = []
    s2 = []
    for i in command:
        if i == '<':
            if s1:
                s2.append(s1.pop())
        elif i == '>':
            if s2:
                s1.append(s2.pop())
        elif i == '-':
            if s1:
                s1.pop()
        else:
            s1.append(i)
    print("".join(s1+list(reversed(s2))))