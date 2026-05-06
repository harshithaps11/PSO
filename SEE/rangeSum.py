def buildPrefix(nums):
    prefix = [0]*(len(nums)+1)
    for i in range (len(nums)):
        prefix[i+1] = prefix[i]+nums[i]
    return prefix
def sumRange(prefix,left,right):
    return prefix[right+1]-prefix[left]
nums = [-2,0,3,-5,2,1]
prefix = buildPrefix(nums)
print(prefix)
print(sumRange(prefix,0,2))
print(sumRange(prefix,2,5))
print(sumRange(prefix,0,5))

