class Solution:
    def maxSubArray(self, nums):
        for i in range(1, len(nums)):
            nums[i] = nums[i] + max(nums[i - 1], 0)
        return max(nums)

    def max2(self, nums):
        ans = nums[0]
        sum = 0
        for num in nums:
            if sum > 0:
                sum += num
            else:
                sum = num
            ans = max(ans, sum)
            print('ans的值是', ans)
            print('sum的值是--', sum)
            print('----------')
        return ans


a = Solution()
print(a.max2([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
