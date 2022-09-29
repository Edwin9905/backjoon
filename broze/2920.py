inpt = list(map(int, input().split()))

if sorted(inpt) == inpt:
    print("ascending")
elif sorted(inpt, reverse=True) == inpt:
    print("descending")
else :
    print("mixed")