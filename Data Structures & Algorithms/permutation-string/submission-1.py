class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        s1Count = [0] * 26
        windowCount = [0] * 26

        #count characters in s1 and the first window of s2
        for i in range(len(s1)):
            s1Count[ord(s1[i]) - ord('a')] += 1
            windowCount[ord(s2[i]) - ord('a')] += 1

        #check the first window
        if s1Count == windowCount:
            return True

        #Slide the window
        left = 0
        for right in range(len(s1), len(s2)):
            windowCount[ord(s2[right]) - ord('a')] += 1

            windowCount[ord(s2[left]) - ord('a')] -= 1

            left += 1
            if s1Count == windowCount:
                return True

        return False
  
