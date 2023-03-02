from typing import List


class Solution:
    def divisibilityArray(self, word: str, m: int) -> List[int]:

        div = []
        p = 0
        for ch in word:
            a = int(ch)
            p = (p*10 + a)%m
            if p%m ==0:
                div.append(1)
            else:
                div.append(0)
        return div
    
if __name__  == '__main__':
    word = "998244353"
    m = 3
    # word = "1010"
    # m = 10
    rtn = Solution().divisibilityArray(word, m)
    print(rtn)