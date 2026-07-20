class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0

        max_length = 1
        l, r = 0, 1
        char = {s[l]}

        while r < len(s):

            if s[r] in char:
                l += 1
                r = l + 1
                char = {s[l]}
            else:
                char.add(s[r])
                max_length = max(max_length, len(char))
                r += 1

        return max_length