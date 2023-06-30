class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # if not s:
        #     return 0
        # left = 0
        # lookup = set()
        # n = len(s)
        # max_len = 0
        # cur_len = 0
        # for i in range(n):
        #     cur_len += 1
        #     while s[i] in lookup:
        #         lookup.remove(s[left])
        #         left += 1
        #         cur_len -= 1
        #     if cur_len > max_len:
        #         max_len = cur_len
        #     lookup.add(s[i])
        # return max_len


        st = set()
        mx = 0
        left, right = 0, 0
        while left < len(s):
            while right < len(s) and (s[right] not in st):
                st.add(s[right])
                right += 1
            mx = max(mx, right - left)
            while right < len(s):
                if s[left] == s[right]:
                    break
                st.remove(s[left])
                left += 1
            st.remove(s[left])
            left += 1
        return mx


if __name__  == '__main__':
    s = ""
    rtn = Solution().lengthOfLongestSubstring(s)
    print(rtn)