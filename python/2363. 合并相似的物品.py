from typing import Counter, List


class Solution:
    def mergeSimilarItems(self, items1: List[List[int]], items2: List[List[int]]) -> List[List[int]]:
        map = Counter()
        for a, b in items1:
            map[a] += b
        for a, b in items2:
            map[a] += b
        return sorted([a, b] for a, b in map.items())
    
if __name__  == '__main__':
    items1 = [[1,1],[4,5],[3,8]]
    items2 = [[3,1],[1,5]]
    items1 = [[1,1],[3,2],[2,3]]
    items2 = [[2,1],[3,2],[1,3]]
    items1 = [[1,3],[2,2]]
    items2 = [[7,1],[2,2],[1,4]]
    rtn = Solution().mergeSimilarItems(items1, items2)
    print(rtn)

