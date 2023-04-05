class Solution:
    def commonFactors(self, a: int, b: int) -> int:
        ans = 1
        m = min(a,b)+1
        for i in range(2, m):
            if a%i ==0 and b%i ==0:
                ans += 1
        return ans
    
if __name__  == '__main__':
    a = 12
    b = 6
    a = 25
    b = 30
    rtn = Solution().commonFactors(a, b)
    print(rtn)