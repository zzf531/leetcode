class Solution(object):
    def maxArea(self, height):
        i = 0
        j = len(height) - 1
        print(j)
        res = 0
        while i < j:
            if height[i] < height[j]:
                res = max(res, height[i] * (j - i))
                i += 1
            else:
                res = max(res, height[j] * (j - i))
                j -= 1
        return res
a = Solution()
print(a.maxArea([1,8,6,2,5,4,8,3,7]))
