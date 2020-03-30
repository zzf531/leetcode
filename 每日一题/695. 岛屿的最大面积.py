
class Solution:


    def maxAreaOfIsland(self, grid):
        ans = 0
        for i, l in enumerate(grid):
            for j, n in enumerate(l):
                ans = max(self.dfs(grid, i, j), ans)
                print('+++老大函数调用')
        return ansdigui

    def dfs(self, grid, cur_i, cur_j):
        if cur_i < 0 or cur_j < 0 or cur_i == len(grid) or cur_j == len(grid[0]) or grid[cur_i][cur_j] != 1:
            print('此时坐标返回零啊', [cur_i, cur_j])
            return 0
        print('此时坐标', [cur_i, cur_j])
        grid[cur_i][cur_j] = 0
        ans = 1
        for di, dj in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
            next_i, next_j = cur_i + di, cur_j + dj
            ans += self.dfs(grid, next_i, next_j)
            print('ans的是',ans)
        return ans

a = Solution()

a2 = [[0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
      [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
      [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0],
      [0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0],
      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
      [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
      [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0]]
print(a.maxAreaOfIsland([[1, 0],
                         [1, 1]]))
