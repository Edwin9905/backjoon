str = input()
start = 'a'
while start <= 'z':
    print(str.find(start), end=" ")
    start = chr(ord(start) + 1)