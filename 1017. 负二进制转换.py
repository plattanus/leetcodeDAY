class Solution:
    def baseNeg2(self, n: int) -> str:
        if n == 0 or n == 1:
            return str(n)
        res = ""
        while n:
            remainder = n & 1
            res = str(remainder) + res
            n -= remainder
            n //= -2
        return res

    
if __name__  == '__main__':
    n = 2
    n = 3
    n = 4
    rtn = Solution().baseNeg2(n)
    print(rtn)