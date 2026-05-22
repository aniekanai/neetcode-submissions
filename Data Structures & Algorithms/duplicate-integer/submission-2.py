class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        #if array is empty, return False
        if len(nums) == 0:
            return False

        #sort the array
        nums.sort()
        #[1, 4, 5, 2, 4] -> [1, 2, 4, 5]

        #iterate through nums
        for i in range(1, len(nums)):
            #if curr equals to prev - checks for duplicates
            if nums[i] == nums[i - 1]:
                return True
            

        # no duplicates found
        return False



     

       
    """ Test cases
        # [1, 2, 2, 4] - > return True
        #[1, 2, 3, 4] -> return False

        #Edge cases
        # [] -> False


        # Possible solution

        satisfy edge case
        if nums is empty:
            return False
        
        # seen = { } check for duplicates -> O(1)
            add elements -> O(1)

        #iterate through the array nums
        #for loop
        #[1, 2, 3, 4, 6]
                      ^ 
            #check is 6 in seen:
                #return True

          #add 1 to the set
             seen = {1, 2, 3, 4, 6} 

        return False

        Time -> O(n) n = len(nums)
        Space -> O(n)
            """


        


