from typing import List


class Solution:
    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:
        n = len(arr)
        j = n - 1
        while j > 0 and arr[j - 1] <= arr[j]:
            j -= 1
        if j == 0:
            return 0
        res = j
        for i in range(n):
            while j < n and arr[j] < arr[i]:
                j += 1
            res = min(res, j - i - 1)
            if i + 1 < n and arr[i] > arr[i + 1]:
                break
        return res

    
if __name__  == '__main__':
    arr = [1,2,3,10,4,2,3,5]
    # arr = [5,4,3,2,1]
    # arr = [1,2,3]
    # arr = [1]
    rtn = Solution().findLengthOfShortestSubarray(arr)
    print(rtn)