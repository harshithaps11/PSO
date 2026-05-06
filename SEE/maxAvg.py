def findMaxAverage(nums, k):
    # Step 1: first window sum
    window_sum = sum(nums[:k])
    max_sum = window_sum

    # Step 2: slide window
    for i in range(k, len(nums)):
        window_sum += nums[i]      # add next
        window_sum -= nums[i - k]  # remove previous

        max_sum = max(max_sum, window_sum)

    return max_sum / k


# example
nums = [1,12,-5,-6,50,3]
k = 4

print(findMaxAverage(nums, k))  # 12.75