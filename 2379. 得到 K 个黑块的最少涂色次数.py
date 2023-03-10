from cmath import inf


class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        
        ans = inf
        cnt = 0 
        for i, ch in enumerate(blocks): 
            if ch == 'W':
                cnt += 1
            if i >= k and blocks[i-k] == 'W':
                cnt -= 1
            if i >= k - 1:
                ans = min(ans, cnt)
        return ans 

if __name__  == '__main__':
    blocks = "WBBWWBBWBW"
    k = 7
    blocks = "WBWBBBW"
    k = 2
    rtn = Solution().minimumRecolors(blocks, k)
    print(rtn)