class Solution:
    def simplifyPath(self, path: str) -> str:

        paths = path.split("/")
        # print(paths)
        stack = []
        for name in paths:
            if name == "..":
                if stack:
                    stack.pop()
            elif name:
                if name == ".":
                    continue
                stack.append(name)

        return "/" + "/".join(stack)


if __name__  == '__main__':
    path = "/home/"
    path = "/../"
    path = "/a/./b/../../c/"
    rtn = Solution().simplifyPath(path)
    print(rtn)