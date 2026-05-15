class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        #declare a set
        seen = set()

        #iterate through the array
        for num in nums:
            #check to see if num in set
            if num in seen:
                return True # num appears more than once

            seen.add(num)

        return False # all numbers appear once
        