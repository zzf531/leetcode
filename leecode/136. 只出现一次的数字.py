class Solution:
    def singleNumber(self, nums):
        a = 0
        for num in nums:
            a ^= num
        return a


a = Solution()
print(a.singleNumber([1, 3, 3, 2, 2]))
