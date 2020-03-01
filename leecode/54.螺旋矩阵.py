class Solution:
    def spiralOrder(self, matrix):
        res = []
        while matrix:
            res += matrix.pop(0)
            matrix = list(map(list, zip(*matrix)))[::-1]
        return res




a = Solution()
print(a.spiralOrder([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]))
