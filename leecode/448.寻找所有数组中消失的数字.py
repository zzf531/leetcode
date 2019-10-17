class Solution(object):
    def findDisappearedNumbers(self, nums):
        for num in nums:
            index = abs(num) - 1
            nums[index] = -abs(nums[index])
        print(nums)
        return [i + 1 for i, num in enumerate(nums) if num > 0]

a = Solution()
print(a.findDisappearedNumbers([4,3,2,7,8,2,3,1]))

#qweqwe
