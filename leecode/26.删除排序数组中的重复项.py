class Solution:
    def removeDuplicates(self, nums):
        i, j = 0, 1
        while j < len(nums):
            if nums[i] == nums[j]:
                nums.pop(j)
            else:
                i += 1
                j += 1
        return len(nums)

a = Solution()
print(a.removeDuplicates([1,1,2,3,4,5,6,6,6]))
