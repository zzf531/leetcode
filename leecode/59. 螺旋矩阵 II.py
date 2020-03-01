class Solution:
    def generateMatrix(self, n):
        r, n = [[n**2]], n**2
        while n > 1: n, r = n - len(r), [[*range(n - len(r), n)]] + [*zip(*r[::-1])]
        return r


a = Solution()
print(a.generateMatrix(4))