class Solution:
    def maskPII(self, s: str) -> str:
        pos = s.find('@')
        if pos > 0:
            return s[0].lower() + "*****" + s[pos-1:].lower()
        s = "".join(i for i in s if i.isdigit())
        return ["", "+*-", "+**-", "+***-"][len(s) - 10] + "***-***-" + s[-4:]

    
if __name__  == '__main__':
    s = "LeetCode@LeetCode.com"
    s = "AB@qq.com"
    s = "1(234)567-890"
    s = "86-(10)12345678"
    rtn = Solution().maskPII(s)
    print(rtn)