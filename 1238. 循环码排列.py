
from typing import List


class Solution:
    def circularPermutation(self, n: int, start: int) -> List[int]:
        ans = [start]
        for i in range(1, n + 1):
            for j in range(len(ans) - 1, -1, -1):
                ans.append(((ans[j] ^ start) | (1 << (i - 1))) ^ start)
        return ans

if __name__  == '__main__':
    n = 2
    start = 3
    n = 3
    start = 2
    rtn = Solution().circularPermutation(n, start)
    print(rtn)