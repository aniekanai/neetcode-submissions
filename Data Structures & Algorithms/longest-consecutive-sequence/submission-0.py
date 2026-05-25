class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        if len(nums) == 0:
            return 0

        numSet = set(nums)
        longest = 0

        for n in nums:
            #check if its the start of a sequence
            if (n - 1) not in numSet:
                length = 0
                while (n + length) in numSet:
                    length += 1
                longest = max(length, longest)
        return longest

        """ #[2, 20, 4, 8, 9, 3, 5]

        # 2, 3, 4, 5 - > 4
        # 8, 9
        # 20 


        Edge Cases
        If the array is empty -> 0

        Solution

        if nums is empty -> 0
        
        # nums_set = {2, 20, 4, 8, 9, 3, 5}
        #seen = {} -> O(1) checking and adding
        #length = 0

        #for num in nums_set:
            check for the start of the sequence
            if 2 - 1 not in seen:
                add to seen
                seen = {2}
                length += 1
                while seen:
                    if 2 + length in num_set:
                        add to seen
                        seen = {2, 3, 4, 5}
                        length += 1

        return lentgh

            

            




        """