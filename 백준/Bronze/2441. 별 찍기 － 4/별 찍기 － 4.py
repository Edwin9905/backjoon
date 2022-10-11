n = int(input())
#while n:
#    print(" "*(5-n)+"*"*n)
#    n -= 1
for i in range(1,n+1) :
    print(" "*(i-1)+"*"*(n+1-i))