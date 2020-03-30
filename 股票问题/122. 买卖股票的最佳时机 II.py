# 因为可以进行无数次交易, 所以算法可以直接简化为只要今天比昨天大，就卖出。
class Solution(object):
    def maxProfit(self, prices):

        res = 0
        for i in range(len(prices) - 1):
            if prices[i + 1] > prices[i]:
                res = res + prices[i + 1] - prices[i]
                print(res, prices[i], prices[i + 1])
        return res


a = Solution()
print(a.maxProfit([7, 1, 5, 3, 6, 4]))
