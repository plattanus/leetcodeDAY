from typing import List


class Solution:
    def checkDistances(self, s: str, distance: List[int]) -> bool:

        appear = [-1 for _ in range(26)]
        for i in range(len(s)):
            t = ord(s[i]) - 97
            if appear[t] == -1:
                appear[t] = i
            else:
                if distance[t] != i - appear[t] - 1:
                    return False
        return True
    

if __name__  == '__main__':
    s = "abaccb"
    distance = [1,3,0,5,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

    s = "aa"
    distance = [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    rtn = Solution().checkDistances(s, distance)
    print(rtn)