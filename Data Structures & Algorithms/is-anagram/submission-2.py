class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        s_pattern = [0] * 26
        t_pattern = [0] * 26

        for char in s:
            s_pattern[ord(char) - ord('a')] += 1

        for char in t:
            t_pattern[ord(char) - ord('a')] += 1

        if s_pattern == t_pattern:
            return True

        return False        