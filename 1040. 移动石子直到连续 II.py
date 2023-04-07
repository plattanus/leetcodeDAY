from typing import List


class Solution:
    def numMovesStonesII(self, stones: List[int]) -> List[int]:
        n = len(stones)
        stones.sort()
        if stones[-1] - stones[0] + 1 == n:
            return [0, 0]
        ma = max(stones[-2] - stones[0] + 1, stones[-1] - stones[1] + 1) - (n - 1)
        mi = n
        j = 0
        for i in range(n):
            while j + 1 < n and stones[j + 1] - stones[i] + 1 <= n:
                j += 1
            if j - i + 1 == n - 1 and stones[j] - stones[i] + 1 == n - 1:
                mi = min(mi, 2)
            else:
                mi = min(mi, n - (j - i + 1))
        return [mi, ma]

if __name__  == '__main__':
    stones = [7,4,9]
    stones = [6,5,4,3,10]
    stones = [100,101,104,102,103]
    rtn = Solution().numMovesStonesII(stones)
    print(rtn)