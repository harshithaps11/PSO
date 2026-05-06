def twoSum(nums, target):
    l = 0
    r = len(nums)-1
    while(l<r):
        s = nums[l] + nums[r]
        if s==target:
            return [l+1,r+1]
        elif s < target:
            l+=1
        else:
            r-=1
print (twoSum([2,7,11,15],9))