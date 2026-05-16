class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        #declare a dictionary
        num_index = {}


        #iterate through the array
        for i in range(len(nums)):
            if target - nums[i] in num_index:
                return [num_index[target - nums[i]], i]
            
            num_index[nums[i]] = i
    

        #return None if no indices can be found
        return None
        