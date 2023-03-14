from typing import List


class Solution:
    def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:
        n, m = len(rowSum), len(colSum)
        matrix = [[0] * m for _ in range(n)]
        i = j = 0
        while i < n and j < m:
            v = min(rowSum[i], colSum[j])
            matrix[i][j] = v
            rowSum[i] -= v
            colSum[j] -= v
            if rowSum[i] == 0:
                i += 1
            if colSum[j] == 0:
                j += 1
        return matrix


if __name__  == '__main__':
    rowSum = [3,8]
    colSum = [4,7]

    rowSum = [5,7,10]
    colSum = [8,6,8]

    rowSum = [14,9]
    colSum = [6,9,8]

    rowSum = [1,0]
    colSum = [1]

    rowSum = [0]
    colSum = [0]
    
    rtn = Solution().restoreMatrix(rowSum, colSum)
    print(rtn)