class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        #sort string s
        s_sorted = "".join(sorted(s))

        #sort string t
        t_sorted = "".join(sorted(t))


        return s_sorted == t_sorted