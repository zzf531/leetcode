# 双指针法
class Solution(object):
    def maxProfit(self, prices):
        res = 0
        if prices:
            min_v = prices[0]
            for i in range(len(prices)):
                if prices[i] < min_v:
                    print('++++')
                    min_v = prices[i]
                if prices[i] - min_v > res:
                    print('---')
                    res = prices[i] - min_v
                print(res, prices[i], min_v)
        return res


a = Solution()
print(a.maxProfit( [7,1,5,3,6,4]))