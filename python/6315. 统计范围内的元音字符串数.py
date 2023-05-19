from typing import List


class Solution:
    def vowelStrings(self, words: List[str], left: int, right: int) -> int:
        s = set()
        s.add('a'); s.add('e'); s.add('i'); s.add('o'); s.add('u')
        ans = 0
        i = 0
        for word in words:
            if left<=i<=right:
                if word[0] in s and word[len(word)-1] in s:
                    ans += 1
            i += 1
        return ans
    
if __name__  == '__main__':
    words = ["are","amy","u"]
    left = 0
    right = 2
    words = ["hey","aeo","mu","ooo","artro"]
    left = 1
    right = 4
    rtn = Solution().vowelStrings(words, left, right)
    print(rtn)