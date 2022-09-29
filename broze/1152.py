str = input()
cnt = str.count(' ') + 1
if str[0] == ' ':
    cnt -= 1
if str[-1] == ' ':
    cnt -= 1
print(cnt)