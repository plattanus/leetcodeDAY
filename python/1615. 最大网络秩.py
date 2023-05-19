from typing import List


class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        count = [0 for _ in range(n)]
        link = [[0]*n for _ in range(n)]
        for i in range(len(roads)):
            link[roads[i][0]][roads[i][1]] = link[roads[i][1]][roads[i][0]] = 1
            count[roads[i][0]] += 1
            count[roads[i][1]] += 1
        mxlink = 0
        for i in range(n):
            for j in range(i+1, n):
                if mxlink < count[i] + count[j] - link[i][j]:
                    mxlink = count[i] + count[j] - link[i][j]
        return mxlink
    
if __name__  == '__main__':
    n = 4
    roads = [[0,1],[0,3],[1,2],[1,3]]
    n = 5
    roads = [[0,1],[0,3],[1,2],[1,3],[2,3],[2,4]]
    n = 8
    roads = [[0,1],[1,2],[2,3],[2,4],[5,6],[5,7]]
    rtn = Solution().maximalNetworkRank(n, roads)
    print(rtn)