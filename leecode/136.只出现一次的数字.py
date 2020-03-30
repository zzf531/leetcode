class Solution:
    def singleNumber(self, nums):
        return 2 * sum(set(nums)) - sum(nums)

    def less1(self, nums):
        for i in nums:
            if nums.count(i) == 1:
                return i


a = Solution()
print(a.singleNumber([1,2,2,3,3]))
print(a.less1([1, 1, 2, 2, 4 ]))
