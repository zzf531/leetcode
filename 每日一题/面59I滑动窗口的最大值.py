class Solution(object):
    def maxSlidingWindow(self, nums, k):
        res = []
        i = 0
        while i < len(nums):
            # res.append(max(nums[i:i+k]))
            print(nums[i:i+k])
            i += k
            print(i)
        return res


a = Solution()
print(a.maxSlidingWindow([1,2,3], 1))