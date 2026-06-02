class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """ #hashmap
        input = [3, 4, 5, 6] target = 7

        output = [0, 1] 

        # num_to_index = {}
        #res = []

        iterate thru nums:

            #check if 7 - 4 in num_to_index
                if not add to map
                num_index = {3 : 0,

                                   
                                   
                                   
                                   }
                else:
                    res = [3 index, 4 index]

        """

        num_to_index = {}
      

        for i in range(len(nums)):
            num = target - nums[i]
            if num in num_to_index:
                return [num_to_index[num], i]
            else:
                num_to_index[nums[i]] = i

        return []


        

            




        


        