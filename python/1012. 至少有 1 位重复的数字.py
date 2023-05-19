from math import perm


class Solution:
    def numDupDigitsAtMostN(self, n: int) -> int:
        limit, s = list(map(int, str(n + 1))), set()
        N, res = len(limit), sum(9 * perm(9, i) for i in range(len(limit) - 1))
        for i, x in enumerate(limit):
            for y in range(i == 0, x):
                if y not in s:
                    res += perm(9 - i, N - i - 1)
            if x in s: 
                break
            s.add(x)
        return n - res

    
if __name__  == '__main__':
    n = 20
    n = 100
    n = 1000
    rtn = Solution().numDupDigitsAtMostN(n)
    print(rtn)