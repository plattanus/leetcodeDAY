from typing import List


class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        n = len(grid)
        ans = [[0] * (n - 2) for _ in range(n - 2)]
        # print(ans)
        for i in range(n - 2):
            for j in range(n - 2):
                ans[i][j] = max(grid[x][y] for x in range(i, i + 3) for y in range(j, j + 3))
        return ans

if __name__  == '__main__':
    grid = [[9,9,8,1],[5,6,2,6],[8,2,6,4],[6,2,2,2]]
    grid = [[1,1,1,1,1],[1,1,1,1,1],[1,1,2,1,1],[1,1,1,1,1],[1,1,1,1,1]]
    rtn = Solution().largestLocal(grid)
    print(rtn)