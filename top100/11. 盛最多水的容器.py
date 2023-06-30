from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        head, tail = 0, len(height)-1
        mx = 0
        while head<tail:
            # mx = max(mx, (tail - head) * min(height[head], height[tail]))
            if height[head] < height[tail]:
                mx = max(mx, (tail - head) * height[head])
                head += 1
            else:
                mx = max(mx, (tail - head) * height[tail])
                tail -= 1
        
        return mx

if __name__  == '__main__':
    height = [1,8,6,2,5,4,8,3,7]
    rtn = Solution().maxArea(height)
    print(rtn)