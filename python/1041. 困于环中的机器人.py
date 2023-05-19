class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        d = [[0,1],[1,0],[0,-1],[-1,0]]
        i = x = y = 0
        for instruction in instructions:
            if instruction == 'G':
                x += d[i][0]
                x += d[i][1]
            elif instruction == 'L':
                i -= 1
                i %= 4
            else:
                i += 1
                i %= 4
        return i != 0 or (x == 0 and y == 0)
    

if __name__  == '__main__':
    instructions = "GGLLGG"
    instructions = "GG"
    instructions = "GL"
    rtn = Solution().isRobotBounded(instructions)
    print(rtn)