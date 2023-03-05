class Solution:
    def passThePillow(self, n: int, time: int) -> int:

        _n = 1
        b = 1
        while time>0:
            if b%2==1:
                _n += 1
            else:
                _n -= 1
            if _n == n or _n == 1:
                b += 1
            time -= 1
        return _n

if __name__  == '__main__':
    n = 4
    time = 5
    n = 3
    time = 2
    rtn = Solution().passThePillow(n, time)
    print(rtn)