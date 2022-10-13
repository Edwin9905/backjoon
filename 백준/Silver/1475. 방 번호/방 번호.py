import math
n = input()
nums = [0] * 10
sixnine = 0
for i in n :
    if int(i) == 6 or int(i) == 9 :
        sixnine += 1
    else :
        nums[int(i)] += 1
sixnine = math.ceil(sixnine/2)
print(max(max(nums),sixnine))