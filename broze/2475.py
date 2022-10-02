nums = list(map(int,input().split(' ')))
powered = [i*i for i in nums]
print(sum(powered)%10)