def moveZeroes(nums):
    for i in range(nums.count(0)):
        nums.remove(0)
        nums.append(0)

    return nums

print(moveZeroes([1,0,0,2,3,4]))
