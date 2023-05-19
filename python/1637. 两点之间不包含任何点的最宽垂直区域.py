from typing import List


class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        a = sorted([point[0] for point in points])
        return max(a[i] - a[i-1] for i in range(1, len(a)))
    

if __name__  == '__main__':
    points = [[8,7],[9,9],[7,4],[9,7]]
    points = [[3,1],[9,0],[1,0],[1,4],[5,3],[8,8]]
    rtn = Solution().maxWidthOfVerticalArea(points)
    print(rtn)
    