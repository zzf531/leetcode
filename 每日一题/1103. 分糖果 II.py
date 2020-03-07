class Solution:
    def d2(self, candies, num_people):
        ans = [0] * num_people
        i = 0
        while candies:
            ans[i % num_people] += min(i + 1, candies)
            candies -= min(i + 1, candies)
            i += 1
        return ans


a = Solution()
print(a.d2(10,3))

