class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0

        max_length = 1
        l, r = 0, 1
        char = set()
        char.add(s[l])
        curr_length = 1
       
        

        while r < len(s):

            if s[r] in char:
                l += 1
                r = l + 1
                char = set()
                char.add(s[l])
                curr_length = 1
            else:
                char.add(s[r])
                curr_length = len(char)
                max_length = max(curr_length, max_length)
                r += 1
        return max_length



        """ 
        input; s = "aacdefghikkl"
                    substring 1 = "acdefghik"
                    kl

        output = 9
`       soluiton
        edge case:

        if string is empty:
            return 0

        
       

        input; s = "aacdefghikkl"
                              lr

        #define 
        max_length = 0
        l = 0, r = 1
        l = 10, r = 12
        while r < 12:
       
        set = { k}
        curr_length = 1
        
        check if s[r] in set: #checkign for duplicates
            #move r forward
            r = 1
            #move l to r previous position -> r - 1 
            l = r - 1 

            #clear the set
            set = {}
            #add s[l]
            set = {k}
            #set curr_lentgh tp 1
            curr_lenght = 1
            
        if s[r] is not in set:
            #add s[r] to our set:
                set = { k, l}
            #caluclate curr_length of set
            curr_length = 2
            #calculayte the maximum lenght seen so far:
            max(curr_length, max_length)
            max_length = 9
            #move r forward

        return max_lenth
        #approach
        two pointer  for calculating length and for moving along the array 
        set  -> check for duplicates 0(1)
        max_length = 0 


        """
        