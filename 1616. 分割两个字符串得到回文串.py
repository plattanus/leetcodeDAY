class Solution:
    def checkPalindromeFormation(self, a: str, b: str) -> bool:

        def check(a: str, left: int, right: int) -> bool:
            while left < right and a[left] == a[right]:
                left += 1
                right -= 1
            return left >= right
        def checkL(a: str, b: str) -> bool:
            n = len(a)
            left, right = 0, n-1
            while left < right and a[left] == b[right]:
                left += 1
                right -= 1
            if left >= right:
                return True
            return check(a, left, right) or check(b, left, right)
        
        return checkL(a, b) or checkL(b, a)
    

if __name__  == '__main__':
    a = "x"
    b = "y"
    a = "abdef"
    b = "fecab"
    a = "ulacfd"
    b = "jizalu"
    rtn = Solution().checkPalindromeFormation(a, b)
    print(rtn)