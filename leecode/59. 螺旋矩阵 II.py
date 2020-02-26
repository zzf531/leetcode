class Solution:
    def generateMatrix(self, n: int):
        res = [[False] * n for _ in range(n)]
        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        x, y = 0, 0
        count = 0

        for i in range(1, n * n + 1):
            res[x][y] = i
            dir_x, dir_y = directions[count][0], directions[count][1]
            if (0 <= x + dir_x < n and 0 <= y + dir_y < n and not res[x + dir_x][y + dir_y]):
                x = x + dir_x
                y = y + dir_y
            else:
                count = (count + 1) % 4
                x = x + directions[count][0]
                y = y + directions[count][1]
        return res


a = Solution()
print(a.generateMatrix(4))