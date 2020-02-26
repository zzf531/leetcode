class Solution(object):
    def subsets(self, nums):
        res = [[]]
        for i in nums:  # 1,2,3
            for num in res:
                res = res + [[i] + num]
            print(res)
        return res


a = Solution()
print(a.subsets([1, 2, 3]))
