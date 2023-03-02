class Solution:
    def printBin(self, num: float) -> str:
        res = "0."
        while len(res) <= 32 and num != 0:
            num *= 2
            digit = int(num)
            res += str(digit)
            num -= digit
        return res if len(res) <= 32 else "ERROR"

if __name__  == '__main__':
    num = 0.625
    num = 0.1
    rtn = Solution().printBin(num)
    print(rtn)