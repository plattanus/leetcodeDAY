
from functools import cache
from itertools import accumulate
from typing import List


class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        
        @cache
        def dfs(pos, m):
            if pos + 2*m >= length:
                return pres[length] - pres[pos]
            # mx = 0
            # for x in range(1, 2*m+1):
            #     mx = max(mx, pres[length]-pres[pos]-dfs(pos+x, max(x,m)))
            # return mx
            return max(pres[length]-pres[pos]-dfs(pos+x, max(x,m)) for x in range(1, 2*m+1))

        length = len(piles)
        pres = list(accumulate(piles, initial=0))

        return dfs(0, 1)

if __name__  == '__main__':
    piles = [2,7,9,4,4]
    piles = [1,2,3,4,5,100]
    rtn = Solution().stoneGameII(piles)
    print(rtn)