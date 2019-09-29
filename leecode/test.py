class Solution:
    def threeSum(self, nums):
        nums.sort()
        res, k = [], 0
        for k in range(len(nums)-2):
            if nums[k] > 0: break
            if k > 0 and nums[k] == nums[k-1]: continue
            j = k+1
            i = len(nums)-1
            while j < i:
                if nums[i] + nums[j] + nums[k] < 0:
                    j += 1
                elif nums[i] + nums[j] + nums[k] > 0:
                    i -= 1
                else:
                    res = res.append(nums[i] + nums[j] + nums[k])
        return res




