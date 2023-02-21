
from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        
        # # 阴影覆盖
        # h1 = height.copy()
        # h2 = height.copy()
        # l = len(height)
        
        # for i in range(1, l):
        #     _i = l-i-1
        #     if h1[i] < h1[i-1]:
        #         h1[i] = h1[i-1]
        #     if h2[_i] < h2[_i+1]:
        #         h2[_i] = h2[_i+1]

        # return sum(h1) + sum(h2) - max(height)*len(height) - sum(height)

        # 单调栈
        stack = []
        sumS = 0
        for i in range(len(height)):
            while stack:
                if height[i] <= height[stack[-1]]:
                    break
                p = stack.pop()
                if stack:
                    sumS += (min(height[i], height[stack[-1]]) -height[p])*(i - stack[-1] - 1)
            stack.append(i)

        return sumS


if __name__  == '__main__':
    height = [0,1,0,2,1,0,1,3,2,1,2,1]
    height = [4,2,0,3,2,5]
    rtn = Solution().trap(height)
    print(rtn)
