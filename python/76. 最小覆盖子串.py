class Solution:
    def minWindow(self, s: str, t: str) -> str:

        m, n = len(s), len(t)
        need = dict()
        win = dict()
        for x in t:
            need[x] = need.get(x, 0) + 1
        match = 0
        start, min_len = 0, m+1
        left, right = 0, 0
        while right<m:
            if s[right] in need:
                win[s[right]] = win.get(s[right], 0) + 1
                if win[s[right]]==need[s[right]]:
                    match += 1
            while match==len(need):
                if right-left+1 < min_len:
                    min_len = right-left+1
                    start = left
                if s[left] in win:
                    win[s[left]] -= 1 
                    if win[s[left]] < need[s[left]]:
                        match -= 1
                left += 1
            right += 1
        if min_len==m+1:
            return ""
        return s[start:start+min_len]

if __name__  == '__main__':
    s = "ADOBECODEBANC"
    t = "ABC"
    s = "a"
    t = "a"
    s = "a"
    t = "aa"
    rtn = Solution().minWindow(s, t)
    print(rtn)