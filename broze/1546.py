input_len = int(input())
lit = map(int,input().split(' '))
lit = list(lit)
max = max(lit)
for i in range(0,input_len):
    lit[i] = round(float(lit[i] / max * 100), 2)
print(sum(lit) / input_len)