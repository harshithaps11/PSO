def characterReplacement(s, k):
    count = {}
    left = 0
    maxf = 0
    res = 0

    for right in range(len(s)):
        count[s[right]] = count.get(s[right], 0) + 1
        maxf = max(maxf, count[s[right]])

        # too many replacements needed → shrink
        if (right - left + 1) - maxf > k:
            count[s[left]] -= 1
            left += 1

        res = max(res, right - left + 1)

    return res


# example
print(characterReplacement("AABABBA", 1))  # 4