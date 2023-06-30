from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        nhR, nhL = 0, 0
        SR, SL, SA, SH = 0, 0, 0, 0
        for i in range(len(height)):
            if height[i] > nhR:
                nhR = height[i]
            SR += nhR
            j = len(height) - i -1
            if height[j] > nhL:
                nhL = height[j]
            SL += nhL
            if height[i] != 0:
                SH += height[i]
        SA = nhR * len(height)
        # return SA - (SA + SA - SR - SL) - SH
        return SR + SL - SA - SH


if __name__  == '__main__':
    height = [0,1,0,2,1,0,1,3,2,1,2,1]
    rtn = Solution().trap(height)
    print(rtn)