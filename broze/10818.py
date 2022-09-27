len = int(input())
nums =input().split(' ')
i = 0
min = int(nums[0])
max = int(nums[0])
while len:
    if max < int(nums[i]):
        max = int(nums[i])
    if min > int(nums[i]):
        min = int(nums[i])
    len -= 1
    i += 1
print (min,max)