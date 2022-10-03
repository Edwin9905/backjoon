input = int(input())
cnt = 1
increse = 6
if input == 1 :
    print(1)
    exit()
input -= 1
while input > 0:
    input -= increse
    cnt += 1
    increse += 6
print(cnt)