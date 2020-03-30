class Solution(object):
    def coinChange(self, coins, amount):
        res = [0 for _ in range(amount + 1)]
        print('res:', res)
        for i in range(1, amount + 1):
            cost = float('inf')
            for c in coins:
                if i - c >= 0:
                    cost = min(cost, res[i - c] + 1)
            res[i] = cost

        if res[amount] == float('inf'):
            return -1
        else:
            return res[amount]


a = Solution()
print(a.coinChange([1, 2, 5], 11))
