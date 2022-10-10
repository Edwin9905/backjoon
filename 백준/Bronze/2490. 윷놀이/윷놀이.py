import sys
for _ in range(3):
    ipt = list(map(int,sys.stdin.readline().strip().split()))
    if ipt.count(1) == 0 :
        print("D")
    elif ipt.count(1) == 1 :
        print("C")
    elif ipt.count(1) == 2 :
        print("B")
    elif ipt.count(1) == 3 :
        print("A")
    elif ipt.count(1) == 4 :
        print("E")
