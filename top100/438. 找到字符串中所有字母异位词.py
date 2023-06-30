from collections import Counter
from typing import List


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        count = Counter(p)
        left, right = 0, 0
        res = []
        while left < len(s):
            while right < len(s) and count[s[right]] > 0:
                count[s[right]] -= 1
                right += 1
            if len(p) == right - left:
                res.append(left)
                # print(left, right)
            if count[s[left]] >= 0:
                count[s[left]] += 1
            left += 1
        return res
    
if __name__  == '__main__':
    s = "cbaebabacd"
    p = "abc"
    rtn = Solution().findAnagrams(s, p)
    print(rtn)