import heapq
from math import inf
from typing import List


class Solution:
    def minimumTime(self, grid: List[List[int]]) -> int:

        m, n = len(grid), len(grid[0])
        if grid[0][1] > 1 and grid[1][0] > 1:
            return -1

        dis = [[inf] * n for _ in range(m)]
        dis[0][0] = 0
        h = [(0, 0, 0)]
        while True:
            d, i, j = heapq.heappop(h)
            if i == m - 1 and j == n - 1:
                return d
            for x, y in (i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1):
                if 0 <= x < m and 0 <= y < n:
                    nd = max(d + 1, grid[x][y])
                    nd += (nd - x - y) % 2
                    if nd < dis[x][y]:
                        dis[x][y] = nd
                        heapq.heappush(h, (nd, x, y))

if __name__  == '__main__':
    grid = [[0,1,3,2],[5,1,2,5],[4,3,8,6]]
    grid = [[0,2,4],[3,2,1],[1,0,4]]
    rtn = Solution().minimumTime(grid)
    print(rtn)