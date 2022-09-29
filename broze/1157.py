input = list(map(str,input().lower()))
alph = [0] * 27
start = 'a'
i = 1
while start <= 'z':
    alph[i] = input.count(start)
    start = chr(ord(start)+1)
    i += 1
if alph.count(max(alph)) > 1:
    print("?")
else :
    print(chr(ord('A') + alph.index((max(alph))) - 1))