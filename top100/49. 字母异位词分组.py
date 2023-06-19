from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        index = 0
        hashtable = dict()
        arr = []
        for stri in strs:
            tstr = ''.join(sorted(stri))
            if tstr in hashtable:
                arr[hashtable[tstr]].append(stri)
            else:
                hashtable[tstr] = index
                index += 1
                arr.append([stri])
        return arr


if __name__  == '__main__':
    strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
    rtn = Solution().groupAnagrams(strs)
    print(rtn)