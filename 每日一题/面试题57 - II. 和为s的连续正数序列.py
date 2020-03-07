class Solution(object):
    def findContinuousSequence(self, target):
        ans = []
        a = target // 2 + 1
        for i in range(1,a):
            res = []
            while sum(res) <= target:
                if sum(res) == target:
                    ans.append(res)
                    break
                res.append(i)
                i += 1
        return ans


a = Solution()
print(a.findContinuousSequence(9))