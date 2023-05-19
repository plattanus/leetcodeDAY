from cmath import inf
from typing import List


class Solution:
    def mergeStones(self, stones: List[int], k: int) -> int:
        n = len(stones)
        if (n - 1) % (k - 1) != 0:
            return -1

        d = [[inf] * n for _ in range(n)]
        sum = [0] * n
        s = 0
        for i in range(n):
            d[i][i] = 0
            s += stones[i]
            sum[i] = s

        for L in range(2, n + 1):
            for l in range(n - L + 1):
                r = l + L - 1
                for p in range(l, r, k - 1):
                    d[l][r] = min(d[l][r], d[l][p] + d[p + 1][r])
                if (r - l) % (k - 1) == 0:
                    d[l][r] += (sum[r] - (0 if l == 0 else sum[l - 1]))
        return d[0][n - 1]


if __name__  == '__main__':
    stones = [3,2,4,1]
    K = 2
    stones = [3,2,4,1]
    K = 3
    stones = [3,5,1,2,6]
    K = 3
    rtn = Solution().mergeStones(stones, K)
    print(rtn)