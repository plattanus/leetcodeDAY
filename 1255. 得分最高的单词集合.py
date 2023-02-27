from typing import List


class Solution:
    def maxScoreWords(self, words: List[str], letters: List[str], score: List[int]) -> int:

        vis = [0 for i in range(26)]
        for letter in letters:
            vis[ord(letter)-ord('a')] += 1

        def check(word) -> bool:
            visT = [0 for i in range(26)]
            for ch in word:
                visT[ord(ch)-ord('a')] += 1
            for i in range(26):
                if vis[i] < visT[i]:
                    return False
            return True

        def Cal(word) -> int:
            sumM = 0
            if check(word):
                for ch in word:
                    sumM += score[ord(ch)-ord('a')]

            return sumM

        self.maxM = 0

        def dfs(strT, pos):
            if pos == len(words):
                if check(strT):
                    self.maxM = max(self.maxM, Cal(strT))
                return
            for i in range(2):
                if i == 0:
                    dfs(strT, pos+1)
                else:
                    dfs(strT+words[pos], pos+1)
        dfs("", 0)
        return self.maxM
    
if __name__  == '__main__':
    words = ["dog","cat","dad","good"]
    letters = ["a","a","c","d","d","d","g","o","o"]
    score = [1,0,9,5,0,0,3,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,0,0,0,0]

    words = ["xxxz","ax","bx","cx"]
    letters = ["z","a","b","c","x","x","x"]
    score = [4,4,4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,5,0,10]

    words = ["leetcode"]
    letters = ["l","e","t","c","o","d"]
    score = [0,0,1,1,1,0,0,0,0,0,0,1,0,0,1,0,0,0,0,1,0,0,0,0,0,0]

    rtn = Solution().maxScoreWords(words, letters, score)
    print(rtn)