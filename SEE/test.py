def characterReplace(s,k):
    count = {}
    left = 0
    res = 0
    maxf = 0
    for right in range(len(s)):
        count[s[right]] = count.get(s[right],0)+1
        maxf = max(maxf,count[s[right]])
        if ( right-left+1) -maxf > k:
            count[s[left]]=1
            left += 1
        res = max ( res,right-left+1)
    return res
print(characterReplace("AABABBA",1))