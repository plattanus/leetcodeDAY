from queue import Queue
from typing import List


class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        d = [[1,0],[0,-1],[-1,0],[0,1]]
        def check(x,y):
            if x>=0 and x<len(grid) and y>=0 and y<len(grid[0]) and grid[x][y] == 0:
                return True
            return False
        
        def position(x,y):
            if x==0 or x==len(grid)-1 or y==0 or y==len(grid[0])-1:
                return True
            return False
        def bfs(x,y):
            que = Queue()
            que.put((x,y))
            res = 1
            while not que.empty():
                q = que.get()
                # print(q)
                if position(q[0],q[1]):
                    res = 0
                for i in range(4):
                    _x = q[0]+d[i][0]
                    _y = q[1]+d[i][1]
                    if check(_x,_y):
                        grid[_x][_y] = -1
                        que.put((_x,_y))
            return res
        res = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0:
                    grid[i][j] = -1
                    res += bfs(i,j)
        return res
    

if __name__  == '__main__':
    grid = [[1,1,1,1,1,1,1,0],[1,0,0,0,0,1,1,0],[1,0,1,0,1,1,1,0],[1,0,0,0,0,1,0,1],[1,1,1,1,1,1,1,0]]
    rtn = Solution().closedIsland(grid)
    print(rtn)