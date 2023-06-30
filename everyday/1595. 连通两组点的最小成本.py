from cmath import inf
from typing import List


class Solution:
    def connectTwoGroups(self, cost: List[List[int]]) -> int:
        size1, size2 = len(cost), len(cost[0])
        m = 1 << size2
        dp = [[inf] * m for _ in range(size1 + 1)]
        dp[0][0] = 0

        for i in range(1, size1 + 1):
            for s in range(m):
                for k in range(size2):
                    if (s & (1 << k)) == 0:
                        continue
                    dp[i][s] = min(dp[i][s], dp[i][s ^ (1 << k)] + cost[i - 1][k])
                    dp[i][s] = min(dp[i][s], dp[i - 1][s] + cost[i - 1][k])
                    dp[i][s] = min(dp[i][s], dp[i - 1][s ^ (1 << k)] + cost[i - 1][k])
        
        return dp[size1][m - 1]

        return 1

if __name__  == '__main__':
    cost = [[1, 3, 5], [4, 1, 1], [1, 5, 3]]
    rtn = Solution().connectTwoGroups(cost)
    print(rtn)