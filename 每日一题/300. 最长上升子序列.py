class Solution(object):
    def lengthOfLIS(self, nums):
        if (not nums):
            return 0
        n = len(nums)
        dp = [1] * n
        for i in range(n):
            print('====')
            for j in range(i):
                print('____')
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)
                    print(dp)
        print(dp)
        return max(dp)

    def dtgh(self, nums):
        lens = len(nums)
        dp = [1] * lens
        if nums:
            for i in range(lens):
                for j in range(i):
                    if nums[i] > nums[j]:
                        dp[i] = max(dp[j] + 1, dp[i])
            return max(dp)
        return 0


a = Solution()
print(a.dtgh([10, 9, 2, 5, 3, 4]))
