class Solution:
    def minimumSwap(self, s1: str, s2: str) -> int:
        
        countX = 0
        countY = 0
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                if s1[i] == 'x':
                    countX += 1
                else:
                    countY += 1
        if (countX + countY)%2 == 0:
            if countX%2 == 0:
                return countX//2 + countY//2
            return countX//2 + countY//2 + 2
        return -1
    
if __name__  == '__main__':
    s1 = "xx"
    s2 = "yy"
    s1 = "xy"
    s2 = "yx"
    s1 = "xx"
    s2 = "xy"
    s1 = "xxyyxyxyxx"
    s2 = "xyyxyxxxyx"
    rtn = Solution().minimumSwap(s1, s2)
    print(rtn)