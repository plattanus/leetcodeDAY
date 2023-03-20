from typing import Deque


class Solution:
    def findLexSmallestString(self, s: str, a: int, b: int) -> str:
        q = Deque([s])
        vis = {s}
        ans = s
        while q:
            s = q.popleft()
            if ans > s:
                ans = s
            t1 = ''.join([str((int(c) + a) % 10) if i & 1 else c for i, c in enumerate(s)])
            t2 = s[-b:] + s[:-b]
            for t in (t1, t2):
                if t not in vis:
                    vis.add(t)
                    q.append(t)
        return ans
    
if __name__  == '__main__':
    s = "5525"
    a = 9
    b = 2

    s = "74"
    a = 5
    b = 1

    s = "0011"
    a = 4
    b = 2

    s = "43987654"
    a = 7
    b = 3
    
    rtn = Solution().findLexSmallestString(s, a, b)
    print(rtn)