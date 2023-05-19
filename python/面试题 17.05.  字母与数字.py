from typing import List


class Solution:
    def findLongestSubarray(self, array: List[str]) -> List[str]:
        indices = {0: -1}
        sum = 0
        maxLength = 0
        startIndex = -1
        for i, s in enumerate(array):
            if '0' <= s[0] <= '9':
                sum += 1
            else:
                sum -= 1
            if sum in indices:
                firstIndex = indices[sum]
                if i - firstIndex > maxLength:
                    maxLength = i - firstIndex
                    startIndex = firstIndex + 1
            else:
                indices[sum] = i
        if maxLength == 0:
            return []
        return array[startIndex: startIndex + maxLength]

if __name__  == '__main__':
    array = ["A","1","B","C","D","2","3","4","E","5","F","G","6","7","H","I","J","K","L","M"]
    array = ["A","A"]
    rtn = Solution().findLongestSubarray(array)
    print(rtn)