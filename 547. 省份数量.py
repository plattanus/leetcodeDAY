from typing import List

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        
        def find(i: int) -> int:
            if fa[i] != i:
                fa[i] = find(fa[i])
            return fa[i]
        
        def merge(i: int, j: int):
            fa[find(i)] = find(j)
        
        cities = len(isConnected)
        fa = list(range(cities))

        for i in range(cities):
            for j in range(i + 1, cities):
                if isConnected[i][j] == 1:
                    merge(i, j)
        
        provinces = sum(fa[i] == i for i in range(cities))
        return provinces



if __name__  == '__main__':
    isConnected = [[1,1,0],[1,1,0],[0,0,1]]
    isConnected = [[1,0,0],[0,1,0],[0,0,1]]
    rtn = Solution().findCircleNum(isConnected)
    print(rtn)