h , m = map(int, input().split())

m -= 45
if m < 0:
    h -= 1
    m = 60 - abs(m)
if h < 0:
    h = 24 - abs(h)
print(h, m)