def rotate(nums, k):
    lenth = len(nums)
    k = k % lenth
    print(k)
    print(nums[lenth - k:] + nums[:lenth - k])
    return nums[-k:] +['A']+ nums[:k+1]


print(rotate([1, 2], 3))
